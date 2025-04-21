# main.py
import os
import sys
import re
import traceback
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel # For request/response models

# --- Reuse necessary imports from your chatbot script ---
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate

# --- Configuration (Match your working chatbot.py) ---
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf" # <--- Use Mistral path
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2" # Embeddings used for the DB
VECTOR_DB_PATH = "./chroma_db_md_meta" # DB path with metadata support
N_CTX = 4096
N_GPU_LAYERS = -1
N_BATCH = 512
MAX_TOKENS_RESPONSE = 350

# --- Global Variables for Loaded Models/DB (Load ONCE on startup) ---
llm = None
vectorstore = None
embeddings = None
QA_CHAIN_PROMPT = None

# --- Pydantic Models for API Request/Response ---
class ChatQuery(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

# --- FastAPI App Initialization ---
app = FastAPI()

# --- Function to Load Models and DB (Run on Startup) ---
def load_resources():
    global llm, vectorstore, embeddings, QA_CHAIN_PROMPT

    print("--- Loading Resources ---")
    # Check paths
    if not os.path.exists(MODEL_PATH):
        print(f"FATAL ERROR: Model file not found at {MODEL_PATH}")
        sys.exit(1)
    if not os.path.isdir(VECTOR_DB_PATH):
        print(f"FATAL ERROR: Vector DB directory '{VECTOR_DB_PATH}' not found.")
        sys.exit(1)

    # Load Embeddings (needed for DB)
    print(f"Loading embedding model '{EMBEDDING_MODEL_NAME}'...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    print("Embedding model loaded.")

    # Load Vector Store
    print(f"Loading existing vector store from '{VECTOR_DB_PATH}'...")
    try:
        vectorstore = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=embeddings
        )
        print(f"Vector store loaded. Contains {vectorstore._collection.count()} documents.")
    except Exception as e:
         print(f"FATAL ERROR: Failed to load vector store. Details: {e}")
         sys.exit(1)

    # Load LLM
    print(f"Loading LLM from '{MODEL_PATH}'...")
    try:
        llm = LlamaCpp(
            model_path=MODEL_PATH,
            n_gpu_layers=N_GPU_LAYERS,
            n_batch=N_BATCH,
            n_ctx=N_CTX,
            max_tokens=MAX_TOKENS_RESPONSE,
            verbose=False,
            f16_kv=True,
        )
        print("LLM loaded.")
    except Exception as e:
        print(f"FATAL ERROR: Failed to load LLM. Details: {e}")
        sys.exit(1)

    # Define Prompt Template
    template = """You are an assistant answering questions based ONLY on the provided documentation context.
If the context includes sections describing features under a specific date or release heading, consider those features as being part of that release.
Answer the user's question directly using the information found in the context.
If the answer cannot be determined from the context, state only: "I cannot answer this question based on the provided documentation."
Do not add apologies or explanations like "Unfortunately..." or "Based on the context...".

Context:
---
{context}
---

Question: {question}

Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    print("--- Resources Loaded Successfully ---")

# --- Run Load Function ON STARTUP ---
# NOTE: In a production scenario, you might use lifespan events,
# but for simplicity, we load directly here. This happens when Uvicorn starts.
load_resources()

# --- Function to get Chatbot Response ---
def get_chatbot_response(user_query: str) -> str:
    """Processes the user query and returns the chatbot answer."""
    if not vectorstore or not llm or not QA_CHAIN_PROMPT:
        # This shouldn't happen if load_resources worked, but safety check
        raise HTTPException(status_code=503, detail="Chatbot resources not loaded")

    try:
        # --- Metadata Filtering Logic ---
        search_filter = None
        year_match = re.search(r'\b(19|20)\d{2}\b', user_query)
        if year_match:
            extracted_year = int(year_match.group(0))
            search_filter = {'year': extracted_year}
            print(f"(API - Filtering for year {extracted_year})")
        else:
            print("(API - No year filter applied)")

        # --- Retrieval Step ---
        retrieved_docs = vectorstore.similarity_search(
            query=user_query,
            k=3,
            filter=search_filter
        )

        # --- Generate final answer ---
        if not retrieved_docs:
             context = ""
             print("(API - No relevant documents found for context)")
             # Return the specific "cannot answer" message if no context found
             return "I cannot answer this question based on the provided documentation."
        else:
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        final_prompt_str = QA_CHAIN_PROMPT.format(context=context, question=user_query)
        final_answer = llm.invoke(final_prompt_str)
        return final_answer.strip()

    except Exception as e:
        print(f"Error during chatbot processing: {e}")
        traceback.print_exc()
        # Return a generic error to the user
        return "Sorry, an error occurred while processing your request."


# --- API Endpoint for Chat ---
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(query: ChatQuery):
    """Receives user query and returns chatbot's answer."""
    print(f"Received query: {query.query}")
    answer = get_chatbot_response(query.query)
    print(f"Sending answer: {answer}")
    return ChatResponse(answer=answer)

# --- Serve Static Files (HTML, CSS, JS) ---
# Mount the 'static' directory at the root URL path '/'
# This means index.html in 'static' will be served for 'http://.../'
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# --- Optional: Root endpoint for testing (can be removed) ---
@app.get("/hello")
def read_root():
    return {"Hello": "World"}

# --- If running directly (optional, usually use uvicorn command) ---
if __name__ == "__main__":
    import uvicorn
    print("Starting Uvicorn server...")
    # Note: Reload=True is good for development, but loads resources multiple times
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)