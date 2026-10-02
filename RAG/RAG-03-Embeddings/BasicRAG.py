# ============================================================
# BASIC RAG - COMPLETE FLOW
# ============================================================
#
# RAG = Retrieval + Augmented + Generation
#
# Flow:
#
# Documents
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
# Top-K Relevant Documents
#     ↓
# Context
#     ↓
# Context + Question
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

# Embedding model
EMBEDDING_MODEL = "nvidia/nemotron-3-embed-1b"

# Chat model
CHAT_MODEL = "openai/gpt-oss-20b"


# ------------------------------------------------------------
# 5. CREATE EMBEDDING
# ------------------------------------------------------------

def create_embedding(text, input_type):
    """
    Convert text into a vector.

    input_type:
        passage -> document
        query   -> user question
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
        a * b for a, b in zip(vector1, vector2)
    )

    # Length of vector 1
    length1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    # Length of vector 2
    length2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    # Cosine similarity
    return dot_product / (length1 * length2)


# ------------------------------------------------------------
# 7. OUR DOCUMENTS
# ------------------------------------------------------------

documents = [
    "Python is used for software development.",
    "Machine learning is a branch of artificial intelligence.",
    "Delhi is the capital of India.",
    "Python can be used to build web applications.",
    "JavaScript is commonly used for web development."
]


# ------------------------------------------------------------
# 8. CREATE VECTOR STORE
# ------------------------------------------------------------

vector_store = []


# ------------------------------------------------------------
# 9. CREATE EMBEDDINGS FOR DOCUMENTS
# ------------------------------------------------------------

for document in documents:

    # Document -> Vector
    vector = create_embedding(
        document,
        "passage"
    )

    # Store text + vector
    vector_store.append({
        "text": document,
        "vector": vector
    })


# ------------------------------------------------------------
# 10. USER QUERY
# ------------------------------------------------------------

query = "What is Python used for?"


# ------------------------------------------------------------
# 11. CREATE QUERY EMBEDDING
# ------------------------------------------------------------

# User Query -> Vector
query_vector = create_embedding(
    query,
    "query"
)


# ------------------------------------------------------------
# 12. SIMILARITY SEARCH
# ------------------------------------------------------------

results = []

for item in vector_store:

    similarity = cosine_similarity(
        query_vector,
        item["vector"]
    )

    results.append({
        "text": item["text"],
        "similarity": similarity
    })


# ------------------------------------------------------------
# 13. SORT RESULTS
# ------------------------------------------------------------

# Highest similarity first
results.sort(
    key=lambda x: x["similarity"],
    reverse=True
)


# ------------------------------------------------------------
# 14. TOP-K
# ------------------------------------------------------------

K = 3

top_results = results[:K]


# ------------------------------------------------------------
# 15. CREATE CONTEXT
# ------------------------------------------------------------

context = "\n".join(
    item["text"]
    for item in top_results
)


# ------------------------------------------------------------
# 16. CREATE RAG PROMPT
# ------------------------------------------------------------

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}

If the answer is not available in the context,
say "I don't know based on the provided context."
"""


# ------------------------------------------------------------
# 17. SEND CONTEXT + QUESTION TO LLM
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
# 18. GET FINAL ANSWER
# ------------------------------------------------------------

answer = response.choices[0].message.content


# ------------------------------------------------------------
# 19. PRINT RESULTS
# ------------------------------------------------------------

print("\n==============================")
print("USER QUERY")
print("==============================")

print(query)


print("\n==============================")
print("TOP K RESULTS")
print("==============================")

for item in top_results:

    print("\nText:")
    print(item["text"])

    print("Similarity:")
    print(item["similarity"])


print("\n==============================")
print("CONTEXT")
print("==============================")

print(context)


print("\n==============================")
print("FINAL ANSWER")
print("==============================")

print(answer)