import os
import sys
import re # Import regular expression module
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import traceback # For error details

# --- Configuration ---
# !!! USER HAS UPDATED THIS PATH to Mistral 7B !!!
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf" # <--- MAKE SURE THIS IS CORRECT
DOCS_DIRECTORY_PATH = "./markdown_docs/"
# --- Embedding model used to BUILD the DB (MiniLM) ---
# We still need this to load the existing DB correctly
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000 # Chunk size used when building the DB
CHUNK_OVERLAP = 200 # Overlap used when building the DB
# --- Vector DB path built with MiniLM + chunk=1000 + metadata ---
VECTOR_DB_PATH = "./chroma_db_md_meta" # <--- Should exist from previous run

# --- LLM Configuration ---
N_CTX = 4096 # Mistral 7B typically supports larger, but 4096 is safe
N_GPU_LAYERS = -1 # Offload all layers to Metal
N_BATCH = 512
MAX_TOKENS_RESPONSE = 350 # Slightly increase for potentially better answers from Mistral

# --- Check if model path exists ---
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: New Model file not found at {MODEL_PATH}")
    sys.exit(1)

# --- Check if docs directory exists ---
if not os.path.isdir(DOCS_DIRECTORY_PATH):
    print(f"ERROR: Documentation directory not found at {DOCS_DIRECTORY_PATH}")
    sys.exit(1)

# --- Check if Vector DB path exists ---
if not os.path.isdir(VECTOR_DB_PATH):
    print(f"ERROR: Vector DB directory '{VECTOR_DB_PATH}' not found.")
    print("Please ensure you ran the script successfully with metadata filtering enabled previously.")
    sys.exit(1)

# --- Load/Split/Embed steps only strictly needed if rebuilding DB ---
# --- We are LOADING the existing DB ---

# --- 3. Setup Embeddings Model (Needed for Loading DB) ---
print(f"Loading embedding model ('{EMBEDDING_MODEL_NAME}') to access vector store...")
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
print("Embedding model loaded.")

# --- 4. Setup Vector Store (Load Existing ChromaDB) ---
print(f"Loading existing vector store from '{VECTOR_DB_PATH}'...")
try:
    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings # Must match the embeddings used to create the DB
    )
    print(f"Vector store loaded. Contains {vectorstore._collection.count()} documents.")
except Exception as e:
     print(f"ERROR: Failed to load vector store from {VECTOR_DB_PATH}. Details: {e}")
     sys.exit(1)


# --- 5. Setup LLM (NOW USING MISTRAL 7B) ---
print(f"Loading LLM from '{MODEL_PATH}'...")
llm = LlamaCpp(
    model_path=MODEL_PATH, # Points to Mistral 7B GGUF
    n_gpu_layers=N_GPU_LAYERS,
    n_batch=N_BATCH,
    n_ctx=N_CTX,
    max_tokens=MAX_TOKENS_RESPONSE,
    # temperature=0.1, # Can try adjusting temperature slightly if needed
    verbose=False,
    f16_kv=True,
)
print("LLM (Mistral 7B) loaded.")

# --- 6. Setup RAG Components (Refined Prompt Template) ---
print("Setting up RAG components...")
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

print("\n--- Setup Complete! Ready to answer questions (Mistral 7B, Clean Output Mode, Updated Prompt). ---")

# --- 7. Interactive Query Loop with Metadata Filtering (Clean Output) ---
while True:
    try:
        user_query = input("\nEnter your question (or type 'quit' to exit): ").strip()
        if user_query.lower() == 'quit':
            print("Exiting chatbot. Goodbye!")
            break
        if not user_query:
            continue

        # --- Metadata Filtering Logic ---
        search_filter = None
        year_match = re.search(r'\b(19|20)\d{2}\b', user_query)
        if year_match:
            extracted_year = int(year_match.group(0))
            search_filter = {'year': extracted_year}
            print(f"(Filtering for year {extracted_year})")
        else:
            print("(No year filter applied)")


        # --- Retrieval Step (Using MiniLM embeddings for query) ---
        # The query is embedded using the loaded MiniLM model to match the DB
        retrieved_docs = vectorstore.similarity_search(
            query=user_query,
            k=3,
            filter=search_filter
        )

        # --- Generate final answer using retrieved docs ---
        if not retrieved_docs:
             context = ""
             print("(No relevant documents found for context)")
        else:
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Format the prompt for the LLM (Mistral)
        final_prompt_str = QA_CHAIN_PROMPT.format(context=context, question=user_query)

        # Invoke the Mistral LLM
        final_answer = llm.invoke(final_prompt_str)

        # --- Print ONLY the LLM's Answer ---
        print(final_answer.strip()) # Print the cleaned-up answer directly

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        # traceback.print_exc() # Uncomment for detailed traceback
    except KeyboardInterrupt:
        print("\nExiting chatbot. Goodbye!")
        break