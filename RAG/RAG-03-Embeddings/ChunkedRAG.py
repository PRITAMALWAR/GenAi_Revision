# ============================================================
# CHUNKED RAG WITH METADATA
# ============================================================
#
# RAG FLOW:
#
# Document
#     ↓
# Chunking
#     ↓
# Chunks
#     ↓
# Embeddings
#     ↓
# Vector Store
#     ↑
# User Query
#     ↓
# Query Embedding
#     ↓
# Similarity Search
#     ↓
# Top-K
#     ↓
# Context
#     ↓
# LLM
#     ↓
# Final Answer
#
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTS
# ------------------------------------------------------------

from openai import OpenAI
from dotenv import load_dotenv
import os
import math


# ------------------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------
# 3. CREATE NVIDIA API CLIENT
# ------------------------------------------------------------

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ------------------------------------------------------------
# 4. MODELS
# ------------------------------------------------------------

EMBEDDING_MODEL = "nvidia/nemotron-3-embed-1b"

CHAT_MODEL = "openai/gpt-oss-20b"


# ------------------------------------------------------------
# 5. CREATE EMBEDDING
# ------------------------------------------------------------

def create_embedding(text, input_type):
    """
    Convert text into a vector.

    passage = document/chunk
    query   = user question
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
        extra_body={
            "input_type": input_type
        }
    )

    return response.data[0].embedding


# ------------------------------------------------------------
# 6. COSINE SIMILARITY
# ------------------------------------------------------------

def cosine_similarity(vector1, vector2):
    """
    Calculate similarity between two vectors.
    """

    # Dot product
    dot_product = sum(
        a * b
        for a, b in zip(vector1, vector2)
    )

    # Vector 1 length
    length1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    # Vector 2 length
    length2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    # Cosine similarity
    return dot_product / (length1 * length2)


# ------------------------------------------------------------
# 7. DOCUMENT
# ------------------------------------------------------------

document = """
Python is a programming language.
Python is easy to learn.
Python is used for software development.
Python can be used to build web applications.
Python is used for artificial intelligence.
Python is used for automation.
Machine learning is a branch of artificial intelligence.
JavaScript is commonly used for web development.
"""


# ------------------------------------------------------------
# 8. DOCUMENT METADATA
# ------------------------------------------------------------

source = "python_notes.txt"


# ------------------------------------------------------------
# 9. CHUNK SETTINGS
# ------------------------------------------------------------

chunk_size = 2
overlap = 1


# ------------------------------------------------------------
# 10. SPLIT DOCUMENT INTO SENTENCES
# ------------------------------------------------------------

sentences = [
    line.strip()
    for line in document.strip().split("\n")
    if line.strip()
]


# ------------------------------------------------------------
# 11. CREATE CHUNKS
# ------------------------------------------------------------

chunks = []

start = 0

while start < len(sentences):

    # Get sentences for current chunk
    chunk_sentences = sentences[
        start:start + chunk_size
    ]

    # Convert list of sentences into one string
    chunk_text = "\n".join(chunk_sentences)

    # Store chunk
    chunks.append(chunk_text)

    # Move forward while keeping overlap
    start += chunk_size - overlap


# ------------------------------------------------------------
# 12. CREATE VECTOR STORE
# ------------------------------------------------------------

vector_store = []


# ------------------------------------------------------------
# 13. CREATE EMBEDDING FOR EACH CHUNK
# ------------------------------------------------------------

for index, chunk in enumerate(chunks):

    # Chunk → Embedding
    vector = create_embedding(
        chunk,
        "passage"
    )

    # Store everything together
    vector_store.append({

        # Metadata
        "chunk_id": index + 1,
        "source": source,

        # Original chunk text
        "text": chunk,

        # Vector representation
        "vector": vector
    })


# ------------------------------------------------------------
# 14. USER QUERY
# ------------------------------------------------------------

query = "What is Python used for?"


# ------------------------------------------------------------
# 15. CREATE QUERY EMBEDDING
# ------------------------------------------------------------

# Query → Embedding
query_vector = create_embedding(
    query,
    "query"
)


# ------------------------------------------------------------
# 16. SIMILARITY SEARCH
# ------------------------------------------------------------

results = []

for item in vector_store:

    # Compare query vector with chunk vector
    similarity = cosine_similarity(
        query_vector,
        item["vector"]
    )

    # Save retrieval result
    results.append({

        "chunk_id": item["chunk_id"],

        "source": item["source"],

        "text": item["text"],

        "similarity": similarity
    })


# ------------------------------------------------------------
# 17. SORT RESULTS
# ------------------------------------------------------------

results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)


# ------------------------------------------------------------
# 18. TOP-K
# ------------------------------------------------------------

K = 3

top_results = results[:K]


# ------------------------------------------------------------
# 19. CREATE CONTEXT
# ------------------------------------------------------------

context_parts = []

for item in top_results:

    context_parts.append(
        f"""
Source: {item["source"]}
Chunk ID: {item["chunk_id"]}

{item["text"]}
"""
    )


context = "\n".join(context_parts)


# ------------------------------------------------------------
# 20. CREATE RAG PROMPT
# ------------------------------------------------------------

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}

If the answer is not available in the context,
say:

"I don't know based on the provided context."
"""


# ------------------------------------------------------------
# 21. SEND CONTEXT + QUESTION TO LLM
# ------------------------------------------------------------

response = client.chat.completions.create(
    model=CHAT_MODEL,

    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],

    temperature=0.2
)


# ------------------------------------------------------------
# 22. GET FINAL ANSWER
# ------------------------------------------------------------

answer = response.choices[0].message.content


# ============================================================
# OUTPUT
# ============================================================


# ------------------------------------------------------------
# 23. PRINT CREATED CHUNKS
# ------------------------------------------------------------

print("\n==============================")
print("CREATED CHUNKS")
print("==============================")

for item in vector_store:

    print(f"\nChunk ID: {item['chunk_id']}")
    print(f"Source: {item['source']}")
    print("Text:")
    print(item["text"])


# ------------------------------------------------------------
# 24. PRINT TOP-K RESULTS
# ------------------------------------------------------------

print("\n==============================")
print("TOP-K RESULTS")
print("==============================")

for item in top_results:

    print("\nChunk ID:")
    print(item["chunk_id"])

    print("Source:")
    print(item["source"])

    print("Text:")
    print(item["text"])

    print("Similarity:")
    print(item["similarity"])


# ------------------------------------------------------------
# 25. PRINT CONTEXT
# ------------------------------------------------------------

print("\n==============================")
print("CONTEXT SENT TO LLM")
print("==============================")

print(context)


# ------------------------------------------------------------
# 26. PRINT FINAL ANSWER
# ------------------------------------------------------------

print("\n==============================")
print("FINAL ANSWER")
print("==============================")

print(answer)