# ============================================================
# PDF -> CHUNKS -> EMBEDDINGS -> VECTOR STORE
# BATCH VERSION
# ============================================================

from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# 2. CREATE NVIDIA API CLIENT
# ============================================================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ============================================================
# 3. MODEL + PDF
# ============================================================

EMBEDDING_MODEL = "nvidia/nemotron-3-embed-1b"

PDF_FILE = "doc/javascript.pdf"


# ============================================================
# 4. CHUNK SETTINGS
# ============================================================

CHUNK_SIZE = 5
OVERLAP = 1

# Kitne chunks ek API request mein jayenge
BATCH_SIZE = 20


# ============================================================
# 5. READ PDF
# ============================================================

reader = PdfReader(PDF_FILE)

print("Total Pages:", len(reader.pages))


# ============================================================
# 6. CREATE CHUNKS
# ============================================================

chunks = []

chunk_id = 1


for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    if not text:
        continue


    # --------------------------------------------------------
    # PDF text -> lines
    # --------------------------------------------------------

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]


    # --------------------------------------------------------
    # Create chunks
    # --------------------------------------------------------

    start = 0

    while start < len(lines):

        chunk_lines = lines[start:start + CHUNK_SIZE]

        chunk_text = "\n".join(chunk_lines)


        chunks.append({
            "chunk_id": chunk_id,
            "source": PDF_FILE,
            "page": page_number,
            "text": chunk_text
        })


        chunk_id += 1

        start += CHUNK_SIZE - OVERLAP


# ============================================================
# 7. SHOW CHUNK INFORMATION
# ============================================================

print("\n==============================")
print("CHUNKING COMPLETE")
print("==============================")

print("Total Chunks:", len(chunks))


# ============================================================
# 8. VECTOR STORE
# ============================================================

vector_store = []


# ============================================================
# 9. CREATE EMBEDDINGS IN BATCHES
# ============================================================

total_chunks = len(chunks)

for start in range(0, total_chunks, BATCH_SIZE):

    # --------------------------------------------------------
    # Current batch
    # --------------------------------------------------------

    batch = chunks[start:start + BATCH_SIZE]


    # --------------------------------------------------------
    # Extract text from batch
    # --------------------------------------------------------

    texts = [
        item["text"]
        for item in batch
    ]


    print(
        f"\nEmbedding chunks "
        f"{start + 1} - {start + len(batch)} "
        f"of {total_chunks}..."
    )


    # --------------------------------------------------------
    # ONE API CALL FOR MULTIPLE CHUNKS
    # --------------------------------------------------------

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
        extra_body={
            "input_type": "passage"
        }
    )


    # --------------------------------------------------------
    # Store embeddings
    # --------------------------------------------------------

    for item, embedding_data in zip(batch, response.data):

        vector_store.append({

            "chunk_id": item["chunk_id"],

            "source": item["source"],

            "page": item["page"],

            "text": item["text"],

            "vector": embedding_data.embedding
        })


# ============================================================
# 10. VECTOR STORE COMPLETE
# ============================================================

print("\n==============================")
print("VECTOR STORE CREATED")
print("==============================")

print("Total Chunks:", len(vector_store))


# ============================================================
# 11. SHOW FIRST 3 RECORDS
# ============================================================

for item in vector_store[:3]:

    print("\n------------------------------")

    print("Chunk ID:", item["chunk_id"])

    print("Source:", item["source"])

    print("Page:", item["page"])

    print("Text:")
    print(item["text"])

    print("Vector Dimension:", len(item["vector"]))


    # ============================================================
# 12. SAVE VECTOR STORE
# ============================================================

import pickle

with open("vector_store.pkl", "wb") as file:
    pickle.dump(vector_store, file)

print("\nVector store saved successfully!")
print("File: vector_store.pkl")