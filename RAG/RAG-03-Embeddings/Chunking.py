# ============================================================
# SIMPLE CHUNKING
# ============================================================

text = """
Python is a programming language.
Python is easy to learn.
Python is used for web development.
Python is used for artificial intelligence.
Python is used for automation.
Python is also used for data analysis.
"""


# ------------------------------------------------------------
# CHUNK SIZE
# ------------------------------------------------------------

chunk_size = 2


# ------------------------------------------------------------
# SPLIT TEXT INTO SENTENCES
# ------------------------------------------------------------

sentences = [
    line.strip()
    for line in text.strip().split("\n")
    if line.strip()
]


# ------------------------------------------------------------
# CREATE CHUNKS
# ------------------------------------------------------------

chunks = []

for i in range(0, len(sentences), chunk_size):

    chunk = sentences[i:i + chunk_size]

    chunks.append(chunk)


# ------------------------------------------------------------
# PRINT CHUNKS
# ------------------------------------------------------------

print("Total Chunks:", len(chunks))


for index, chunk in enumerate(chunks):

    print("\n--------------------")
    print("Chunk", index + 1)
    print("--------------------")

    print("\n".join(chunk))