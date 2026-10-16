# GenAi_Revision


- 1. Create a virtual environment

python3 -m venv .venv
sudo apt install python3-venv


- 2. Activate it

source .venv/bin/activate


- 3. Upgrade pip

python -m pip install --upgrade pip


- 4. Install your packages

pip install agno streamlit openai groq ddgs


- 5. Then run your agent

python agent.py


<!-- ============= Tokens ==================== -->

- pip install tiktoken
- pip show tiktoken


```
Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
LLM

```


# 1. AI & LLM Basics

## 1. What is AI (Artificial Intelligence)?


Computer ko aise kaam karwana jisme normally human intelligence ki zarurat padti hai.

Examples:

- Face recognition
- Voice recognition
- Recommendation systems
- Chatbots
- Self-driving systems
- Fraud detection

```
Tum → "Mujhe ek laptop suggest karo"

AI → Tumhari requirement samjhega
   → Available options analyze karega
   → Recommendation dega
```

Interview-ready answer :

Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making.

Interview example: A recommendation system analyzes user preferences and suggests relevant products, movies, or videos.

## 2. What is Generative AI?

Simple Meaning (Hinglish):

Generative AI naya content generate kar sakta hai.

Examples:

- Text: ChatGPT, Claude, Gemini
- Image: AI image generators
- Code: Coding assistants
- Audio: Voice generation
- Video: AI video generators

Interview-ready answer :

Generative AI is a type of artificial intelligence that learns patterns from training data and uses those patterns to generate new content, such as text, images, code, audio, and video.

Interview example: ChatGPT can generate an explanation, while an image-generation model can create an image from a text prompt.

Key difference: Traditional AI often predicts, classifies, or makes decisions; Generative AI focuses on creating new content. Some systems can do both.

## 3. What is an LLM (Large Language Model)?

Simple Meaning (Hinglish):

LLM ek AI model hai jo human language ko process aur generate karne ke liye large amounts of text data par train hota hai.

Examples:

- GPT
- Claude
- Gemini
- Llama
- Mistral

Example:

```
User:
"Explain React in simple words."

        ↓

       LLM

        ↓

"React is a JavaScript library..."
```

Interview-ready answer:

A Large Language Model (LLM) is a deep learning model trained on large amounts of text to understand and generate language. It can perform tasks such as question answering, summarization, translation, text generation, and code generation.

How does an LLM generate text?

An LLM processes the input as tokens and predicts the next token based on the preceding context. It repeats this process to generate a response.

## 4. What is a Token?

Simple Meaning (Hinglish):

LLM directly words ko process nahi karta; text ko tokens mein break karta hai. Token ek word, word ka part, punctuation ya koi aur text unit ho sakta hai.

Example:

Input:

```
"Hello, how are you?"
```

Roughly tokens mein break ho sakta hai:

```
Hello | , | how | are | you | ?
```

Exact tokenization model ke according different ho sakti hai.

Interview-ready answer:

A token is a basic unit of text processed by a language model. Depending on the tokenizer, a token can represent a complete word, part of a word, punctuation, or another text unit. Models process input and generate output in tokens.

Interview follow-up: Why are tokens important?

Tokens affect the context window, API usage, processing cost, and the maximum amount of input and output a model can handle.

## 5. What is Context?

Simple Meaning (Hinglish):

Context = woh poori relevant information/input jo LLM ke paas response generate karte waqt available hoti hai.

Isme include ho sakta hai:

- Current prompt
- Previous conversation
- Documents / retrieved information
- Tool results
- Instructions / system information
- Relevant memory

Example:

```
User: My name is Rahul.
Assistant: Nice to meet you!

User: What is my name?

LLM → Available conversation context use karega
    → Answer: Rahul
```

Agar previous conversation model ko available nahi hai, toh woh information answer karne ke liye use nahi kar sakta.

Interview-ready answer (English):

Context is the information available to an LLM when it generates a response. It may include the current prompt, conversation history, system instructions, retrieved documents, and tool results. The quality and relevance of the context strongly influence the response.

Interview follow-up: What happens if context is missing?

The model may misunderstand the question, produce an incomplete answer, or make unsupported assumptions.

## 6. What is a Context Window?

Simple Meaning (Hinglish):

Context window = model ek request/conversation mein kitni information tokens ke form mein handle kar sakta hai.

Example:

```
User Message
     +
System Prompt
     +
Previous Conversation
     +
Documents
     +
Tool Results
     ↓
Context Window
     ↓
    LLM
     ↓
   Output
```

Agar context bahut bada ho jaye, model ki token limit aa sakti hai.

Interview-ready answer (English):

A context window is the maximum amount of tokenized information a language model can process within a single context. It can include input instructions, conversation history, documents, tool results, and generated output, depending on the model and its architecture.

Interview follow-up: How can we handle context window limitations?

- Chunk large documents.
- Retrieve only relevant information using RAG.
- Summarize older conversation history.
- Remove irrelevant content.
- Manage input and output token budgets.

Important difference:

| Context                                   | Context Window                                  |
| ----------------------------------------- | ----------------------------------------------- |
| Actual information available to the model | Maximum token capacity for that context         |
| Example: prompt and documents             | Example: model supports a specified token limit |

## 7. How Can We Use an LLM?

Simple Meaning (Hinglish):

LLM ko application mein use karne ke 3 common ways hain:

[Getting Started with Ollama - Hongkiat](https://images.openai.com/static-rsc-4/Wx4lB_K5MHEXQQSNVpChcIxDTsTlMbXTtNh7OkUP4D2AbMsZevfFHyIR00r0tXUIrQrYjxaC0gRedVeKm81ZVjzeBOvv4CXoRTrcnKMOOdDaCpxkIONbmPuKvkESy9riG2qh7uWPUOon1pJcJD3GypHg1eH83ZKOrlB09MInmWE?purpose=inline)

1\. Run LLM Locally

Apne computer par model run karna.

Example: Ollama + Llama

Use case: Local experimentation, offline use where supported, and greater control over data handling.

[Microsoft Improves Position In Artificial Intelligence…](https://images.openai.com/static-rsc-4/K_dh3CVVaYwEASY4LWVNxFhzvcf0h5foJcBPcq2UvPtKPL5JtFxYXqIr6yIQVhPrvkX7IwD6N9AKhHvGa7NtvkBXyN0VKHMM_F2VYx4iI9yJ1bwWZW1CKgCYX2wLqaigM7dF8AKFq88IYspTzR3UvD1NgGnUoO99JEHE3SDPl9k?purpose=inline)

2\. Self-host / Deploy LLM on Cloud

Apne server ya cloud infrastructure par model deploy karna.

Example: Llama deployed on your server.

Use case: Custom deployment, infrastructure control, and serving multiple users.

[API and AI technologies. Business workflow automation. Platform for AI integration and data communication.](https://images.openai.com/static-rsc-4/cHfJImgGXkHgrtPC5X8WbtaAVtzKOJppwZL6gPu4UWwe143jPzZ1yPO_B9klhSu0crg7EnIVDJVKoCjVTrVjFXY_XuixVtaURpQHgRLKKkZJ5iwzldK0wbRGZfc1dFPLEaIgAH0p63IEnSuoKqgrrQWcJ6yTuhESoi-bNWj21pIcr4lsWzOghYpsiaQx4S9l?purpose=inline)

3\. Use a Hosted LLM API

Provider ke hosted model ko API request bhejkar use karna.

Examples: OpenAI API, Gemini API, Claude API.

Use case: Quickly integrating an LLM into an application without managing model-serving infrastructure.

Simple architecture:

```
                LLM
                 |
        -------------------
        |        |        |
      LOCAL    CLOUD     API
        |        |        |
      Ollama  Your Server Provider
        |        |        |
      Llama    Llama     GPT/Gemini
```

Interview-ready answer:

There are three common ways to use an LLM in an application: run an open-weight model locally, self-host a model on your own cloud infrastructure, or consume a hosted LLM through a provider's API.

The choice depends on latency, cost, privacy requirements, scalability, infrastructure capabilities, and maintenance effort.

Interview follow-up: Which approach would you choose for a production application?

A hosted API is often the simplest starting point because it reduces infrastructure management. Local or self-hosted models may be preferable when data control, customization, predictable workloads, or infrastructure economics justify the additional operational effort.

## 8. Complete LLM Processing Flow

Your tokenization diagram can be understood as follows:

User Prompt

"What is JavaScript?"

Tokenization

Text → Input tokens

LLM Processing

Uses model parameters and available context

Next-Token Prediction

Generates output tokens iteratively

Final Response

Output tokens → Readable text

Interview-ready answer :

An LLM application converts the input text into tokens, processes those tokens using the model and its available context, and generates output tokens iteratively. The tokenizer then converts the generated token sequence into readable text.

