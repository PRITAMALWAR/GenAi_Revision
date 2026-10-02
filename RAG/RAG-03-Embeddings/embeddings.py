from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()


# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
)


# Text that we want to convert into an embedding
text = "I love Python"


# Generate embedding
response = client.embeddings.create(
    model="nvidia/nemotron-3-embed-1b",
    input=text,
    extra_body={
        "input_type": "passage"
    }
)


# Get the embedding vector
embedding = response.data[0].embedding


print("Text:")
print(text)

print("\nEmbedding Preview:")
print([round(x, 2) for x in embedding[:10]])


print("\nNumber of dimensions:")
print(len(embedding))