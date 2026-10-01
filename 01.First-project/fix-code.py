from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

# 1. Load environment variables
load_dotenv()

# 2. Create API client
client = OpenAI(
    api_key=getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

# 3. Get user input
text = input("Enter text: ")

# 4. Create prompt
prompt = f"""
Summarize the following text in 3 simple sentences:

{text}
"""

# 5. Send request to AI
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# 6. Extract AI response
summary = response.choices[0].message.content

# 7. Display result
print("\nSummary:")
print(summary)