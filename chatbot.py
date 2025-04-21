import os
import sys
import re
import time # Import time for measuring re-ranking latency (optional)
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.prompts import PromptTemplate
# --- Import CrossEncoder ---
from sentence_transformers import CrossEncoder
import traceback

# --- Configuration ---
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf" # Mistral 7B
DOCS_DIRECTORY_PATH = "./markdown_docs/"
# --- Using BGE embeddings and large chunks DB ---
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
VECTOR_DB_PATH = "./chroma_db_md_bge_large" # Assumes this exists
CHUNK_SIZE = 2000 # Keep large chunk size
CHUNK_OVERLAP = 400 # Keep large overlap
# --- Re-ranker Configuration ---
CROSS_ENCODER_MODEL_NAME = 'cross-encoder/ms-marco-MiniLM-L-6-v2'
INITIAL_RETRIEVAL_K = 15 # Retrieve more docs initially
FINAL_CONTEXT_K = 3 # Use top N docs after re-ranking for final context

# --- LLM Configuration ---
N_CTX = 4096
N_GPU_LAYERS = -1
N_BATCH = 512
MAX_TOKENS_RESPONSE = 350

# --- Global Variables ---
llm = None
vectorstore = None
embeddings = None
QA_CHAIN_PROMPT = None
cross_encoder = None # Variable for the re-ranker model

# --- Check paths ---
if not os.path.exists(MODEL_PATH):
    print(f"FATAL ERROR: Model file not found at {MODEL_PATH}")
    sys.exit(1)
if not os.path.isdir(DOCS_DIRECTORY_PATH):
    print(f"FATAL ERROR: Documentation directory not found at {DOCS_DIRECTORY_PATH}")
    sys.exit(1)
if not os.path.isdir(VECTOR_DB_PATH):
    print(f"FATAL ERROR: Vector DB directory '{VECTOR_DB_PATH}' not found.")
    sys.exit(1)

# --- Load Resources on Startup ---
def load_resources():
    global llm, vectorstore, embeddings, QA_CHAIN_PROMPT, cross_encoder

    print("--- Loading Resources ---")
    # Load Embeddings
    print(f"Loading embedding model '{EMBEDDING_MODEL_NAME}'...")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
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

    # Load Cross-Encoder Model
    print(f"Loading Cross-Encoder model '{CROSS_ENCODER_MODEL_NAME}'...")
    try:
        cross_encoder = CrossEncoder(CROSS_ENCODER_MODEL_NAME)
        print("Cross-Encoder model loaded.")
    except Exception as e:
        print(f"FATAL ERROR: Failed to load Cross-Encoder model. Details: {e}")
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
load_resources()

# --- FastAPI App Initialization ---
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class ChatQuery(BaseModel):
    query: str
class ChatResponse(BaseModel):
    answer: str

app = FastAPI()

# --- Function to get Chatbot Response with Re-ranking ---
def get_chatbot_response(user_query: str) -> str:
    """Processes query, retrieves, re-ranks, and generates answer."""
    if not vectorstore or not llm or not QA_CHAIN_PROMPT or not cross_encoder:
        raise HTTPException(status_code=503, detail="Chatbot resources not loaded")

    try:
        print(f"(API - Retrieving initial {INITIAL_RETRIEVAL_K} candidates)")
        # --- 1. Initial Retrieval (No Metadata Filter Needed Now) ---
        # Retrieve more candidates based on embedding similarity
        retrieved_docs = vectorstore.similarity_search(
            query=user_query,
            k=INITIAL_RETRIEVAL_K
        )

        if not retrieved_docs:
             print("(API - No documents found in initial retrieval)")
             return "I cannot answer this question based on the provided documentation."

        # --- 2. Re-ranking Step ---
        print(f"(API - Re-ranking {len(retrieved_docs)} candidates with Cross-Encoder...)")
        start_time = time.time()
        # Prepare pairs for the cross-encoder: [ [query, doc_content1], [query, doc_content2], ... ]
        rerank_pairs = [[user_query, doc.page_content] for doc in retrieved_docs]
        # Predict scores
        scores = cross_encoder.predict(rerank_pairs)
        # Combine docs with their scores
        docs_with_scores = list(zip(retrieved_docs, scores))
        # Sort by score in descending order
        docs_with_scores.sort(key=lambda x: x[1], reverse=True)
        # Select the top N after re-ranking
        reranked_docs = [doc for doc, score in docs_with_scores[:FINAL_CONTEXT_K]]
        end_time = time.time()
        print(f"(API - Re-ranking took {end_time - start_time:.2f} seconds)")

        # --- 3. Generate final answer ---
        print("(API - Generating final answer from re-ranked context)")
        context = "\n\n".join([doc.page_content for doc in reranked_docs])
        final_prompt_str = QA_CHAIN_PROMPT.format(context=context, question=user_query)
        final_answer = llm.invoke(final_prompt_str)

        # Optionally print sources based on re-ranking for debugging
        # print("\n--- Re-ranked Sources ---")
        # for i, doc in enumerate(reranked_docs):
        #     source = doc.metadata.get('source', 'Unknown')
        #     print(f"{i+1}. Source: {source}\n   Content: {doc.page_content[:200]}...\n")

        return final_answer.strip()

    except Exception as e:
        print(f"Error during chatbot processing: {e}")
        traceback.print_exc()
        return "Sorry, an error occurred while processing your request."


# --- API Endpoint for Chat ---
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(query: ChatQuery):
    """Receives user query and returns chatbot's answer."""
    print(f"Received query: {query.query}")
    answer = get_chatbot_response(query.query)
    print(f"Sending answer: {answer}")
    return ChatResponse(answer=answer)

# --- Serve Static Files ---
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# --- If running directly (optional) ---
# if __name__ == "__main__":
#     import uvicorn
#     print("Starting Uvicorn server...")
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)