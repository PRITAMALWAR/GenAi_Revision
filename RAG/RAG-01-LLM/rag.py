from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Explain RAG only 1 line."
)

print(response.output_text)