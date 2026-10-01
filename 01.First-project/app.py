from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = OpenAI(
    api_key=getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "what is javascript"
        }
    ],
)

print(response.choices[0].message.content)