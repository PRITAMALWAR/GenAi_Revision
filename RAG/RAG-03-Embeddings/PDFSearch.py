# ============================================================
# PDF RAG
# Query -> Embedding -> Similarity -> Top-K -> Context -> LLM
# ============================================================

from openai import OpenAI
from dotenv import load_dotenv
import os
import pickle
import math


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# 2. CREATE NVIDIA CLIENT
# ============================================================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ============================================================
# 3. MODELS
# ============================================================

EMBEDDING_MODEL = "nvidia/nemotron-3-embed-1b"

CHAT_MODEL = "openai/gpt-oss-20b"


# ============================================================
# 4. LOAD VECTOR STORE
# ============================================================

with open("vector_store.pkl", "rb") as file:
    vector_store = pickle.load(file)


print("Vector Store Loaded")
print("Total Chunks:", len(vector_store))


# ============================================================
# 5. USER QUERY
# ============================================================

query = input("\nAsk a question about the PDF: ")


# ============================================================
# 6. CREATE QUERY EMBEDDING
# ============================================================

response = client.embeddings.create(
    model=EMBEDDING_MODEL,
    input=query,
    extra_body={
        "input_type": "query"
    }
)

query_vector = response.data[0].embedding


# ============================================================
# 7. COSINE SIMILARITY
# ============================================================

def cosine_similarity(vector1, vector2):

    dot_product = sum(
        a * b
        for a, b in zip(vector1, vector2)
    )

    length1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    length2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    return dot_product / (length1 * length2)


# ============================================================
# 8. SIMILARITY SEARCH
# ============================================================

results = []


for item in vector_store:

    score = cosine_similarity(
        query_vector,
        item["vector"]
    )

    results.append({

        "chunk_id": item["chunk_id"],

        "source": item["source"],

        "page": item["page"],

        "text": item["text"],

        "score": score
    })


# ============================================================
# 9. SORT RESULTS
# ============================================================

results.sort(
    key=lambda x: x["score"],
    reverse=True
)


# ============================================================
# 10. TOP-K
# ============================================================

K = 5

top_results = results[:K]


# ============================================================
# 11. CREATE CONTEXT
# ============================================================

context_parts = []


for result in top_results:

    context_parts.append(
        f"""
Source: {result["source"]}
Page: {result["page"]}
Chunk ID: {result["chunk_id"]}

{result["text"]}
"""
    )


context = "\n".join(context_parts)


# ============================================================
# 12. SHOW RETRIEVED CONTEXT
# ============================================================

print("\n==============================")
print("RETRIEVED CONTEXT")
print("==============================")

print(context)


# ============================================================
# 13. CREATE RAG PROMPT
# ============================================================

prompt = f"""
Answer the user's question using only the provided context.

If the answer is not available in the context,
say that the information is not available in the provided PDF context.

Context:
{context}

User Question:
{query}
"""


# ============================================================
# 14. SEND CONTEXT + QUESTION TO LLM
# ============================================================

response = client.chat.completions.create(

    model=CHAT_MODEL,

    messages=[

        {
            "role": "system",
            "content": "You answer questions using the provided PDF context."
        },

        {
            "role": "user",
            "content": prompt
        }

    ],

    temperature=0.2
)


# ============================================================
# 15. FINAL ANSWER
# ============================================================

answer = response.choices[0].message.content


print("\n==============================")
print("FINAL ANSWER")
print("==============================")

print(answer)