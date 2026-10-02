import tiktoken


text = """
I love India
"""


encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Tokens:" ,tokens)
print( "Text:", text)


print("Character count:", len(text))
print("Token count:", len(tokens))



# Words
words = text.split()
print("words:" ,words)


for token in tokens:
    print(token, "=", encoding.decode([token]))