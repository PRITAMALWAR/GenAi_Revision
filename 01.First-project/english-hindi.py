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
text = input("Enter English text: ")

# 4. Create prompt
prompt = f"""
Translate the following English text into Hindi.

English:
{text}

Return only the Hindi translation.
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
translation = response.choices[0].message.content

# 7. Display output
print("\nHindi:", translation)