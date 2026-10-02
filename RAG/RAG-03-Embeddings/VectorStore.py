# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import math


# # ============================================================
# # 1. Load environment variables
# # ============================================================

# load_dotenv()


# # ============================================================
# # 2. Create NVIDIA client
# # ============================================================

# client = OpenAI(
#     base_url="https://integrate.api.nvidia.com/v1",
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# MODEL = "nvidia/nemotron-3-embed-1b"


# # ============================================================
# # 3. Create embedding
# # ============================================================

# def create_embedding(text, input_type):

#     response = client.embeddings.create(
#         model=MODEL,
#         input=text,
#         extra_body={
#             "input_type": input_type
#         }
#     )

#     return response.data[0].embedding


# # ============================================================
# # 4. Cosine similarity
# # ============================================================

# def cosine_similarity(vector1, vector2):

#     dot_product = sum(
#         a * b for a, b in zip(vector1, vector2)
#     )

#     length1 = math.sqrt(
#         sum(a * a for a in vector1)
#     )

#     length2 = math.sqrt(
#         sum(b * b for b in vector2)
#     )

#     return dot_product / (length1 * length2)


# # ============================================================
# # 5. Our documents
# # ============================================================

# documents = [
#     "Python is used for software development.",
#     "Machine learning is a branch of artificial intelligence.",
#     "Delhi is the capital of India."
# ]


# # ============================================================
# # 6. Create our mini Vector Store
# # ============================================================

# vector_store = []


# for document in documents:

#     vector = create_embedding(
#         document,
#         "passage"
#     )

#     vector_store.append({
#         "text": document,
#         "vector": vector
#     })


# # ============================================================
# # 7. User Query
# # ============================================================

# query = "What is Python used for?"


# # Query → query embedding
# query_vector = create_embedding(
#     query,
#     "query"
# )


# # ============================================================
# # 8. Search Vector Store
# # ============================================================

# results = []


# for item in vector_store:

#     similarity = cosine_similarity(
#         query_vector,
#         item["vector"]
#     )

#     results.append({
#         "text": item["text"],
#         "similarity": similarity
#     })


# # ============================================================
# # 9. Sort results
# # ============================================================

# results.sort(
#     key=lambda item: item["similarity"],
#     reverse=True
# )


# # ============================================================
# # 10. Print results
# # ============================================================

# print("User Query:")
# print(query)

# print("\nSearch Results:")

# for result in results:

#     print("\nText:")
#     print(result["text"])

#     print("Similarity:")
#     print(result["similarity"])




# ======================================================================================
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
# 4. Cosine similarity
# ============================================================

def cosine_similarity(vector1, vector2):

    dot_product = sum(
        a * b for a, b in zip(vector1, vector2)
    )

    length1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    length2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    return dot_product / (length1 * length2)


# ============================================================
# 5. Documents
# ============================================================

documents = [
    "Python is used for software development.",
    "Machine learning is a branch of artificial intelligence.",
    "Delhi is the capital of India.",
    "Python can be used to build web applications.",
    "JavaScript is commonly used for web development."
]


# ============================================================
# 6. Create Vector Store
# ============================================================

vector_store = []


for document in documents:

    vector = create_embedding(
        document,
        "passage"
    )

    vector_store.append({
        "text": document,
        "vector": vector
    })


# ============================================================
# 7. User Query
# ============================================================

query = "What is Python used for?"


# Query → embedding
query_vector = create_embedding(
    query,
    "query"
)


# ============================================================
# 8. Similarity Search
# ============================================================

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


# ============================================================
# 9. Sort by similarity
# ============================================================

results.sort(
    key=lambda item: item["similarity"],
    reverse=True
)


# ============================================================
# 10. Top-K
# ============================================================

K = 3

top_results = results[:K]


# ============================================================
# 11. Print Top-K results
# ============================================================

print("User Query:")
print(query)

print("\nTop", K, "Results:")

for result in top_results:

    print("\nText:")
    print(result["text"])

    print("Similarity:")
    print(result["similarity"])