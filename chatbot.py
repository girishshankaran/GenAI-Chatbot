import os
import sys # Import sys to exit gracefully
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Import DirectoryLoader and UnstructuredMarkdownLoader
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- Configuration ---
# !!! IMPORTANT: Replace with the ACTUAL path to your model file !!!
MODEL_PATH = "/Users/gisankar/Documents/GenAI-Project/models/Llama-3.2-3B-Instruct-Q4_K_M.gguf" # <--- CHANGE THIS
# !!! IMPORTANT: Set this to the DIRECTORY containing your Markdown files !!!
DOCS_DIRECTORY_PATH = "./markdown_docs/" # <--- CHANGE THIS
VECTOR_DB_PATH = "./chroma_db_md" # Using a different directory for the MD-based DB
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# --- LLM Configuration ---
N_CTX = 4096
N_GPU_LAYERS = -1
N_BATCH = 512
MAX_TOKENS_RESPONSE = 256

# --- Check if model path exists ---
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: Model file not found at {MODEL_PATH}")
    sys.exit(1) # Exit if model is not found

# --- Check if docs directory exists ---
if not os.path.isdir(DOCS_DIRECTORY_PATH):
    print(f"ERROR: Documentation directory not found at {DOCS_DIRECTORY_PATH}")
    print("Please create it and add your Markdown files.")
    sys.exit(1)

# --- 1. Load Documentation from Directory ---
print(f"Loading Markdown documents from '{DOCS_DIRECTORY_PATH}'...")
# Use DirectoryLoader to load all .md files using UnstructuredMarkdownLoader
loader = DirectoryLoader(
    DOCS_DIRECTORY_PATH,
    glob="**/*.md",  # Load all .md files recursively
    loader_cls=UnstructuredMarkdownLoader,
    show_progress=True, # Show progress bar during loading
    use_multithreading=True # Use threads for faster loading if many files
)
documents = loader.load()

if not documents:
    print(f"ERROR: No Markdown documents found in '{DOCS_DIRECTORY_PATH}'.")
    sys.exit(1)

print(f"Loaded {len(documents)} Markdown document(s).")

# --- 2. Chunk Documentation ---
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    # Try to split based on Markdown structures first
    separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " ", ""],
    length_function=len,
)
texts = text_splitter.split_documents(documents)
print(f"Split into {len(texts)} text chunks.")

# --- 3. Setup Embeddings Model ---
print(f"Loading embedding model '{EMBEDDING_MODEL_NAME}'...")
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
print("Embedding model loaded.")

# --- 4. Setup Vector Store (ChromaDB) ---
print(f"Creating/loading vector store at '{VECTOR_DB_PATH}'...")
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory=VECTOR_DB_PATH
)
vectorstore.persist()
print("Vector store created/updated.")

# --- 5. Setup LLM (LlamaCpp with Metal) ---
print(f"Loading LLM from '{MODEL_PATH}'...")
llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_gpu_layers=N_GPU_LAYERS,
    n_batch=N_BATCH,
    n_ctx=N_CTX,
    max_tokens=MAX_TOKENS_RESPONSE,
    # temperature=0.75,
    # top_p=0.9,
    verbose=False, # Set verbose=False to avoid flooding console during interactive use
    f16_kv=True,
)
print("LLM loaded.")

# --- 6. Setup RAG Chain ---
print("Setting up RAG chain...")
template = """Use the following pieces of context ONLY to answer the question at the end.
If you don't know the answer from the context, just say that you don't know, don't try to make up an answer.
Keep the answer concise.

Context:
{context}

Question: {question}

Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)
print("\n--- Setup Complete! Ready to answer questions. ---")

# --- 7. Interactive Query Loop ---
while True:
    try:
        user_query = input("\nEnter your question (or type 'quit' to exit): ").strip()
        if user_query.lower() == 'quit':
            print("Exiting chatbot. Goodbye!")
            break
        if not user_query:
            continue # Skip empty input

        print("Processing...")
        result = qa_chain.invoke(user_query) # Use invoke for LangChain v0.1+

        print("\n--- Answer ---")
        print(result["result"])

        # Optional: Print sources if you want to see them during interaction
        # print("\n--- Sources ---")
        # unique_sources = {}
        # for doc in result["source_documents"]:
        #     source_path = doc.metadata.get('source', 'Unknown')
        #     unique_sources[doc.page_content] = source_path
        # if unique_sources:
        #     for i, source in enumerate(unique_sources.items()):
        #         print(f"{i+1}. Content: {source[0][:100]}... (Source: {source[1]})")
        # else:
        #     print("No relevant sources found in the context.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    except KeyboardInterrupt: # Allow graceful exit with Ctrl+C
        print("\nExiting chatbot. Goodbye!")
        break