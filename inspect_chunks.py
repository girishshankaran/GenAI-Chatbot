# inspect_chunks.py
import os
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# --- Configuration ---
# !!! Make sure this path points to your 2025 file !!!
DOC_PATH = "./markdown_docs/sea_release_notes/2025.md" # Adjust if path is different
# !!! Use the chunk size we were trying !!!
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 400

# --- Check if doc path exists ---
if not os.path.exists(DOC_PATH):
    print(f"ERROR: Document file not found at {DOC_PATH}")
    sys.exit(1)

# --- 1. Load Specific Documentation ---
print(f"Loading Markdown document from '{DOC_PATH}'...")
loader = UnstructuredMarkdownLoader(DOC_PATH)
documents = loader.load()

if not documents:
    print(f"ERROR: Failed to load document '{DOC_PATH}'.")
    sys.exit(1)

print(f"Loaded {len(documents)} document object(s). Expecting 1.")

# --- 2. Chunk Documentation ---
print(f"Splitting document using chunk_size={CHUNK_SIZE}, chunk_overlap={CHUNK_OVERLAP}...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " ", ""],
    length_function=len,
)
texts = text_splitter.split_documents(documents) # 'texts' is a list of Document objects
print(f"Split into {len(texts)} text chunks.")

# --- 3. Print Chunks ---
print("\n--- Generated Chunks ---")
if texts:
    for i, chunk_doc in enumerate(texts):
        print(f"\n--- Chunk {i+1} (Length: {len(chunk_doc.page_content)}) ---")
        print(chunk_doc.page_content) # Print the actual text content of the chunk
        print("-" * 20) # Separator
else:
    print("No chunks were generated.")
