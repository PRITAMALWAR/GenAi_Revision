import tiktoken


# ============================================================
# STEP 1: Text → Token IDs
# ============================================================

text = "Pritam"

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("=" * 50)
print("STEP 1: Text → Token IDs")
print("=" * 50)

print("Text:", text)
print("Token IDs:", tokens)


# ============================================================
# STEP 2: Text → Tokens → Decode back to Text
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: Encode and Decode")
print("=" * 50)

print("Original text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nNumber of tokens:")
print(len(tokens))

print("\nDecoded text:")
print(encoding.decode(tokens))


# ============================================================
# STEP 3: Multiple Text Examples
# ============================================================

print("\n" + "=" * 50)
print("STEP 3: Multiple Text Examples")
print("=" * 50)

texts = [
    "Hello",
    "Hello world",
    "I love AI",
    "Hello Rudra",
    "Generative Artificial Intelligence",
    "Hello, how are you?",
]

for text in texts:

    tokens = encoding.encode(text)

    print("\n" + "-" * 40)
    print("Text:", text)
    print("Token IDs:", tokens)
    print("Token count:", len(tokens))


# ============================================================
# STEP 4: Token ID → Token
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: Token ID → Token")
print("=" * 50)

text = "I love AI"

tokens = encoding.encode(text)

print("Text:", text)
print("Token IDs:", tokens)

for token_id in tokens:

    token_text = encoding.decode([token_id])

    print(
        f"Token ID = {token_id} | Token = '{token_text}'"
    )


# ============================================================
# STEP 5: Token Details + Character Count
# ============================================================

print("\n" + "=" * 50)
print("STEP 5: Token Details")
print("=" * 50)

text = "pritam"

token_ids = encoding.encode(text)

print("Text =", text)
print("Tokens =", len(token_ids))
print("Characters =", len(text))

print("\nToken Details:")

for token_id in token_ids:

    token_text = encoding.decode([token_id])

    print(
        f"Token ID = {token_id} | Token = '{token_text}'"
    )