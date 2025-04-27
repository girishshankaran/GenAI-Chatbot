# main.py (Metadata Filtering, MiniLM, Mistral LLM, chunk=1000 - WITH BUILD LOGIC)
import os
import sys
import re
import traceback
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# --- LangChain & Model Imports ---
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.prompts import PromptTemplate

# --- Configuration ---
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf" # Mistral path
DOCS_DIRECTORY_PATH = "./markdown_docs/"
# --- Configuration for this Metadata Filtering setup ---
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2" # MiniLM Embeddings
CHUNK_SIZE = 1000 # Smaller chunk size
CHUNK_OVERLAP = 200 # Smaller overlap
VECTOR_DB_PATH = "./chroma_db_md_meta" # DB path for this setup
# --- Retrieval K value ---
RETRIEVAL_K = 3 # How many docs to retrieve

# --- LLM Configuration ---
N_CTX = 4096
N_GPU_LAYERS = -1
N_BATCH = 512
MAX_TOKENS_RESPONSE = 350 # Original token limit

# --- Global Variables ---
llm = None
vectorstore = None
embeddings = None
QA_CHAIN_PROMPT = None

# --- Pydantic Models ---
class ChatQuery(BaseModel): query: str
class ChatResponse(BaseModel): answer: str

# --- FastAPI App Initialization ---
app = FastAPI()

# --- Function to Load Resources (Handles DB Creation/Loading) ---
def load_resources():
    global llm, vectorstore, embeddings, QA_CHAIN_PROMPT

    print("--- Loading Resources ---")
    # --- Check Core Paths ---
    if not os.path.exists(MODEL_PATH): sys.exit(f"FATAL ERROR: LLM file not found at {MODEL_PATH}")
    if not os.path.isdir(DOCS_DIRECTORY_PATH): sys.exit(f"FATAL ERROR: Docs directory not found at {DOCS_DIRECTORY_PATH}")

    # --- Load Embeddings ---
    print(f"Loading embedding model '{EMBEDDING_MODEL_NAME}'...")
    try:
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
        print("Embedding model loaded.")
    except Exception as e: sys.exit(f"FATAL ERROR: Failed to load embedding model. Details: {e}")

    # --- Load or Build Vector Store ---
    rebuild_db = False
    if os.path.isdir(VECTOR_DB_PATH):
        print(f"Loading existing vector store from '{VECTOR_DB_PATH}'...")
        try:
            vectorstore = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
            if vectorstore._collection.count() == 0:
                 print(f"WARNING: Vector store at {VECTOR_DB_PATH} is empty. Forcing rebuild.")
                 rebuild_db = True
                 vectorstore = None # Ensure it's None to trigger rebuild
            else:
                 print(f"Vector store loaded. Contains {vectorstore._collection.count()} documents.")
        except Exception as e:
             print(f"ERROR: Failed to load vector store from {VECTOR_DB_PATH}. Forcing rebuild. Details: {e}")
             rebuild_db = True
             vectorstore = None
    else:
        print(f"Vector store not found at '{VECTOR_DB_PATH}'. Building...")
        rebuild_db = True # Set flag to build

    if rebuild_db:
        try:
            # 1. Load Docs & Add Metadata
            print(f"Loading Markdown documents from '{DOCS_DIRECTORY_PATH}' and extracting year metadata...")
            md_loader = DirectoryLoader(
                DOCS_DIRECTORY_PATH, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader,
                show_progress=True, use_multithreading=True,
            )
            documents = []
            loaded_docs = md_loader.load()
            print(f"Loaded {len(loaded_docs)} initial document objects.")
            for doc in loaded_docs:
                source_path = doc.metadata.get('source', '')
                if source_path:
                    filename = os.path.basename(source_path)
                    year_match = re.search(r'(19|20)\d{2}', filename)
                    doc.metadata['year'] = int(year_match.group(0)) if year_match else 0
                documents.append(doc)
            if not documents: sys.exit("ERROR: No documents processed after loading. Cannot build DB.")
            print(f"Processed {len(documents)} documents with year metadata (if found).")

            # 2. Chunk Docs
            print(f"Splitting documents (chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})...")
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
                separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " ", ""], length_function=len,
            )
            texts = text_splitter.split_documents(documents)
            if not texts: sys.exit("ERROR: No text chunks generated after splitting. Cannot build DB.")
            print(f"Split into {len(texts)} text chunks.")

            # 3. Create and Persist DB
            print(f"Creating vector store at '{VECTOR_DB_PATH}'...")
            vectorstore = Chroma.from_documents(
                documents=texts, embedding=embeddings, persist_directory=VECTOR_DB_PATH
            )
            vectorstore.persist()
            print(f"Vector store created and persisted. Contains {vectorstore._collection.count()} documents.")

        except Exception as e:
            print(f"FATAL ERROR: Failed during vector store build process. Details: {e}")
            traceback.print_exc()
            sys.exit(1)

    # --- Load LLM ---
    print(f"Loading LLM from '{MODEL_PATH}'...")
    try:
        llm = LlamaCpp(
            model_path=MODEL_PATH, n_gpu_layers=N_GPU_LAYERS, n_batch=N_BATCH, n_ctx=N_CTX,
            max_tokens=MAX_TOKENS_RESPONSE, verbose=False, f16_kv=True,
        )
        print("LLM loaded.")
    except Exception as e: sys.exit(f"FATAL ERROR: Failed to load LLM. Details: {e}")

    # --- Define Prompt Template ---
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
load_resources()

# --- Pydantic Models ---
class ChatQuery(BaseModel): query: str
class ChatResponse(BaseModel): answer: str

# --- Function to get Chatbot Response ---
def get_chatbot_response(user_query: str) -> str:
    if not vectorstore or not llm or not QA_CHAIN_PROMPT:
        raise HTTPException(status_code=503, detail="Chatbot resources not initialized")

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
            k=RETRIEVAL_K, # Using config variable k=3
            filter=search_filter
        )

        # --- Generate final answer ---
        if not retrieved_docs:
             context = ""
             print("(API - No relevant documents found for context)")
             # Let the LLM handle the empty context based on the prompt
        else:
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        final_prompt_str = QA_CHAIN_PROMPT.format(context=context, question=user_query)
        final_answer = llm.invoke(final_prompt_str)

        # Handle case where LLM might still output the fallback phrase even with context
        # (Less likely with Mistral 7B but good practice)
        fallback_phrase = "I cannot answer this question based on the provided documentation."
        if not retrieved_docs and fallback_phrase not in final_answer:
             # If no docs were found, force the fallback phrase if LLM didn't say it
             return fallback_phrase
        elif final_answer.strip() == fallback_phrase and retrieved_docs:
             # If docs WERE found but LLM *still* couldn't answer, keep its response
             pass # Allow the LLM's "cannot answer" response

        return final_answer.strip()

    except Exception as e:
        print(f"Error during chatbot processing: {e}")
        traceback.print_exc()
        return "Sorry, an error occurred while processing your request."


# --- API Endpoint for Chat ---
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(query: ChatQuery):
    print(f"Received query: {query.query}")
    answer = get_chatbot_response(query.query)
    print(f"Sending answer: {answer}")
    return ChatResponse(answer=answer)

# --- Serve Static Files ---
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# --- Optional root endpoint ---
@app.get("/hello")
def read_root(): return {"Hello": "World"}

# --- Main block ---
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)