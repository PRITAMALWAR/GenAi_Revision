from openai import OpenAI
from dotenv import load_dotenv
import os
import math


# ============================================================
# 1. Load environment variables
# ============================================================

load_dotenv()


# ============================================================
# 2. Create NVIDIA client
# ============================================================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


# Embedding model
MODEL = "nvidia/nemotron-3-embed-1b"


# ============================================================
# 3. Create embedding
# ============================================================

def create_embedding(text, input_type):

    response = client.embeddings.create(
        model=MODEL,
        input=text,
        extra_body={
            "input_type": input_type
        }
    )

    return response.data[0].embedding


# ============================================================
# 4. Calculate cosine similarity
# ============================================================

def cosine_similarity(vector1, vector2):

    # Multiply corresponding values
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


# ============================================================
# 5. Document and User Query
# ============================================================

document = "Python is used for software development."

query = "What is Python used for?"


# ============================================================
# 6. Create embeddings
# ============================================================

# Document → passage
document_vector = create_embedding(
    document,
    "passage"
)

# User question → query
query_vector = create_embedding(
    query,
    "query"
)


# ============================================================
# 7. Compare document and query
# ============================================================

similarity = cosine_similarity(
    document_vector,
    query_vector
)


# ============================================================
# 8. Print results
# ============================================================

print("Document:")
print(document)

print("\nUser Query:")
print(query)

print("\nDocument Embedding Dimensions:")
print(len(document_vector))

print("\nQuery Embedding Dimensions:")
print(len(query_vector))

print("\nSimilarity:")
print(similarity)