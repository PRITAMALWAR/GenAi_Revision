# Step 1 text convet token


import tiktoken

text = "Pritam"

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print(tokens)





# Step 2 text convet token

# import tiktoken

# text = "Pritam"

# encoding = tiktoken.get_encoding("cl100k_base")

# tokens = encoding.encode(text)

# print("Original text:")
# print(text)

# print("\nToken IDs:")
# print(tokens)

# print("\nNumber of tokens:")
# print(len(tokens))

# print("\nDecoded text:")
# print(encoding.decode(tokens))





# Step 3

# import tiktoken

# encoding = tiktoken.get_encoding("cl100k_base")

# texts = [
#     "Hello",
#     "Hello world",
#     "I love AI",
#     "Generative Artificial Intelligence",
#     "Hello, how are you?",
# ]

# for text in texts:
#     tokens = encoding.encode(text)

#     print("=" * 40)
#     print("Text:", text)
#     print("Token IDs:", tokens)
#     print("Token count:", len(tokens))



# step 4

# import tiktoken

# encoding = tiktoken.get_encoding("cl100k_base")

# text = "I love AI"

# tokens = encoding.encode(text)

# print("Text:", text)
# print("Token IDs:", tokens)

# for token_id in tokens:
#     print("Token ID:", token_id)




#step 5

import tiktoken

text = "pritam"

encoding = tiktoken.get_encoding("cl100k_base")

token_ids = encoding.encode(text)

print("Text =", text)
print("Tokens =", len(token_ids))
print("Characters =", len(text))

print("\nToken Details:")

for token_id in token_ids:
    token_text = encoding.decode([token_id])
    print(f"Token ID = {token_id}  |  Token = '{token_text}'")
