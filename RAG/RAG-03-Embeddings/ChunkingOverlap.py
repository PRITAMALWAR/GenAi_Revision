# ============================================================
# CHUNKING + OVERLAP
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
# CHUNK SETTINGS
# ------------------------------------------------------------

chunk_size = 2
overlap = 1


# ------------------------------------------------------------
# SPLIT TEXT INTO SENTENCES
# ------------------------------------------------------------

sentences = [
    line.strip()
    for line in text.strip().split("\n")
    if line.strip()
]


# ------------------------------------------------------------
# CREATE CHUNKS WITH OVERLAP
# ------------------------------------------------------------

chunks = []

start = 0

while start < len(sentences):

    # Get chunk
    chunk = sentences[start:start + chunk_size]

    chunks.append(chunk)

    # Move forward
    start += chunk_size - overlap


# ------------------------------------------------------------
# PRINT CHUNKS
# ------------------------------------------------------------

print("Total Chunks:", len(chunks))


for index, chunk in enumerate(chunks):

    print("\n====================")
    print("Chunk", index + 1)
    print("====================")

    print("\n".join(chunk))