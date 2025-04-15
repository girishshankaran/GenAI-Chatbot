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
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
DOCS_DIRECTORY_PATH = "./markdown_docs/"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000 # Smaller chunk size
CHUNK_OVERLAP = 200 # Smaller overlap
VECTOR_DB_PATH = "./chroma_db_md_meta" # DB path with metadata support

# --- LLM Configuration ---
N_CTX = 4096
N_GPU_LAYERS = -1
N_BATCH = 512
MAX_TOKENS_RESPONSE = 256

# --- Check if model path exists ---
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: Model file not found at {MODEL_PATH}")
    sys.exit(1)

# --- Check if docs directory exists ---
if not os.path.isdir(DOCS_DIRECTORY_PATH):
    print(f"ERROR: Documentation directory not found at {DOCS_DIRECTORY_PATH}")
    sys.exit(1)

# --- Check if Vector DB path exists (it should from previous run) ---
if not os.path.isdir(VECTOR_DB_PATH):
    print(f"ERROR: Vector DB directory '{VECTOR_DB_PATH}' not found.")
    print("Please ensure you ran the script successfully with metadata filtering enabled.")
    sys.exit(1)


# --- Load/Split/Embed steps only strictly needed if rebuilding DB ---
# --- Assume DB exists for faster startup on subsequent runs ---


# --- 3. Setup Embeddings Model ---
# Needed for loading the vector store
print(f"Loading embedding model '{EMBEDDING_MODEL_NAME}'...")
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
print("Embedding model loaded.")

# --- 4. Setup Vector Store (Load Existing ChromaDB) ---
# This will *load* the existing DB.
print(f"Loading existing vector store from '{VECTOR_DB_PATH}'...")
try:
    vectorstore = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings # Provide embedding function for loading
    )
    print(f"Vector store loaded. Contains {vectorstore._collection.count()} documents.")
except Exception as e:
     print(f"ERROR: Failed to load vector store from {VECTOR_DB_PATH}. Details: {e}")
     sys.exit(1)


# --- 5. Setup LLM (LlamaCpp with Metal) ---
print(f"Loading LLM from '{MODEL_PATH}'...")
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

# --- 6. Setup RAG Components (Prompt Template) ---
print("Setting up RAG components...")
# --- Modified Prompt Template for more direct answers ---
template = """Answer the following question based ONLY on the provided context.
Provide only the direct answer to the question, without explanations or apologies like "Unfortunately..." or "Based on the context...".
If the answer is not found in the context, state only: "I cannot answer this question based on the provided documentation."

Context:
---
{context}
---

Question: {question}

Answer:""" # Using "Answer:" helps focus the LLM
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

print("\n--- Setup Complete! Ready to answer questions (Clean Output Mode). ---")

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
            print(f"(Filtering for year {extracted_year})") # Minimal processing message
        else:
            print("(No year filter applied)") # Minimal processing message


        # --- Retrieval Step ---
        retrieved_docs = vectorstore.similarity_search(
            query=user_query,
            k=3, # Retrieve top 3 matching chunks
            filter=search_filter # Apply the year filter if available
        )

        # --- Generate final answer using retrieved docs ---
        if not retrieved_docs:
             # Handle case where filter returns no documents
             # Option 1: Print a standard message
             # print("No relevant documentation found for the specified criteria.")
             # Option 2: Pass empty context to LLM, relying on the prompt's instruction
             context = "" # Set context to empty if no docs found
             print("(No relevant documents found for context)") # Minimal processing message
        else:
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # Format the prompt
        final_prompt_str = QA_CHAIN_PROMPT.format(context=context, question=user_query)

        # Invoke LLM
        final_answer = llm.invoke(final_prompt_str)

        # --- Print ONLY the LLM's Answer ---
        print(final_answer.strip()) # Print the cleaned-up answer directly


        # --- Source Printing Block Removed ---


    except Exception as e:
        print(f"\nAn error occurred: {e}")
        # traceback.print_exc() # Uncomment for detailed traceback during debugging
    except KeyboardInterrupt:
        print("\nExiting chatbot. Goodbye!")
        break