

import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = """
Generative AI is a type of artificial intelligence
that can generate new content such as text, images,
audio, video, and code.
"""


tokens = encoding.encode(text)

print("Characters:", len(text))
print("Tokens:", len(tokens))
print("Token IDs:", tokens)