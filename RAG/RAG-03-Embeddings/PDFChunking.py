# ============================================================
# PDF TEXT -> CHUNKS
# ============================================================

from pypdf import PdfReader


# ------------------------------------------------------------
# 1. PDF FILE
# ------------------------------------------------------------

PDF_FILE = "doc/javascript.pdf"


# ------------------------------------------------------------
# 2. CHUNK SETTINGS
# ------------------------------------------------------------

chunk_size = 5
overlap = 1


# ------------------------------------------------------------
# 3. READ PDF
# ------------------------------------------------------------

reader = PdfReader(PDF_FILE)

print("Total Pages:", len(reader.pages))


# ------------------------------------------------------------
# 4. EXTRACT TEXT FROM PDF
# ------------------------------------------------------------

all_text = ""

for page_number, page in enumerate(reader.pages):

    text = page.extract_text()

    if text:
        all_text += text + "\n"


# ------------------------------------------------------------
# 5. SPLIT TEXT INTO LINES
# ------------------------------------------------------------

lines = [
    line.strip()
    for line in all_text.split("\n")
    if line.strip()
]


# ------------------------------------------------------------
# 6. CREATE CHUNKS
# ------------------------------------------------------------

chunks = []

start = 0

while start < len(lines):

    # Get current chunk
    chunk_lines = lines[
        start:start + chunk_size
    ]

    # Convert lines into one text block
    chunk_text = "\n".join(chunk_lines)

    # Save chunk
    chunks.append(chunk_text)

    # Move forward while keeping overlap
    start += chunk_size - overlap


# ------------------------------------------------------------
# 7. PRINT CHUNKS
# ------------------------------------------------------------

print("\n==============================")
print("TOTAL CHUNKS")
print("==============================")

print(len(chunks))


# ------------------------------------------------------------
# 8. PRINT EACH CHUNK
# ------------------------------------------------------------

for index, chunk in enumerate(chunks):

    print("\n==============================")
    print(f"CHUNK {index + 1}")
    print("==============================")

    print(chunk)