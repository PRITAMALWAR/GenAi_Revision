# AI & LLM Basics — LangChain Notes

## 1. What is LangChain?

Simple Meaning (Hinglish):

Maan lo tumhe Gemini AI ka use karke chatbot banana hai. Tum directly Gemini SDK use kar sakte ho, lekin jab application mein prompts, message history, tools, RAG aur multiple model providers manage karne hon, tab LangChain helpful ho sakta hai.

LangChain khud AI model nahi hai. Ye tumhari application aur AI model ke beech integration layer provide karta hai.

Your Node.js Application

User questions and instructions

LangChain

Messages · Prompts · Model calls · Tools · Output

LLM

Gemini / OpenAI / Groq-supported models

Interview-ready answer (English):

LangChain is a framework for building applications powered by large language models. It provides abstractions for model integration, prompt management, message handling, tool calling, retrieval, and other components used in LLM applications.

Why do we use LangChain?

- To integrate supported LLM providers through a consistent interface.
- To manage system and human messages.
- To build prompt templates and chains.
- To connect models with tools and external data.
- To implement retrieval-augmented generation (RAG).

## 2. What is a Chat Model?

Simple Meaning (Hinglish):

Chat model ek AI model interface hai jo messages receive karta hai aur response generate karta hai.

Tumhare examples mein teen model integrations hain:

| Provider              | LangChain class / function | Purpose                                                              |
| --------------------- | -------------------------- | -------------------------------------------------------------------- |
| Google Gemini         | `ChatGoogleGenerativeAI`   | Gemini chat models                                                   |
| Groq                  | `ChatGroq`                 | Groq-hosted models                                                   |
| Universal initializer | `initChatModel`            | Supported model integrations ko common interface se initialize karna |

Interview-ready answer (English):

A chat model is an interface to a language model that accepts conversational messages and generates a response. In LangChain, chat models support a common invocation pattern, although provider-specific configuration and capabilities can differ.

## 3. What is a Message Role?

Simple Meaning (Hinglish):

Chatbot mein har message ka ek role hota hai, jo batata hai ki message kis purpose se aaya hai.

| Role               | Meaning                          | Example                          |
| ------------------ | -------------------------------- | -------------------------------- |
| `system`           | AI ka behaviour aur instructions | You are a coding teacher         |
| `human`            | User ka message                  | Explain React                    |
| `assistant` / `ai` | AI ka response                   | React is a UI library            |
| `tool`             | Tool execution ka result         | Search result or database output |

Dhyan do: `system` aur `human` message roles hain. `assistant` AI ke response ko represent karta hai, aur `tool` tool execution se aaya result represent karta hai. Exact supported role formats framework aur provider ke according vary kar sakte hain.

### Example from your code

```
const result = await ai.invoke([
    {
        role: "system",
        content: "You are Jarvis, my personal AI assistant."
    },
    {
        role: "human",
        content: prompt
    }
]);
```

Is code mein:

1. System message AI ko behaviour instructions deta hai.
2. Human message user ka actual prompt contain karta hai.
3. `ai.invoke()` messages ko model tak bhejta hai.
4. Model response return karta hai.

Interview-ready answer (English):

Message roles identify the purpose or source of a message in a conversation. A system message provides instructions, a human message contains user input, an AI message represents the model's response, and a tool message contains the result returned by a tool.

## 4. What is `invoke()` in LangChain?

Simple Meaning (Hinglish):

`invoke()` ka use model ko input dene aur uska response receive karne ke liye hota hai.

### Method 1: Direct prompt

```
// Send a simple text prompt to the model
const result = await model.invoke(
    "Explain React in simple English"
);

// Read the generated response
console.log(result.text);
```

### Method 2: Messages with roles

```
const result = await ai.invoke([
    {
        role: "system",
        content: "You are Jarvis, my personal AI assistant."
    },
    {
        role: "human",
        content: "Explain React in simple English."
    }
]);

// Read the model response
console.log(result.content);
```

Difference:

- `model.invoke(prompt)` — simple prompt-based invocation.
- `ai.invoke(messages)` — message-based invocation with roles and instructions.

The exact response shape can depend on the model integration. For standard LangChain `AIMessage` responses, `.content` contains the response content, while `.text` is a convenient text accessor in supported versions.

Interview-ready answer (English):

The `invoke()` method sends an input to a LangChain runnable, such as a chat model, and returns its result. It can accept a string or structured messages, depending on the component being invoked.

## 5. What is a System Prompt?

Simple Meaning (Hinglish):

System prompt AI ko batata hai ki usse kaise behave karna hai, kis tarah answer dena hai, aur kis role mein kaam karna hai.

Example:

```
{
    role: "system",
    content: "You are Jarvis, my personal AI assistant."
}
```

Iske baad user agar poochta hai:

```
Explain JavaScript functions.
```

Toh model system instructions ko follow karne ki koshish karega aur JavaScript functions explain karega.

Interview-ready answer (English):

A system prompt provides high-level instructions that guide an LLM's behavior, response style, and task objectives. It helps establish how the model should respond to user inputs.

Important: A system prompt guides the model but does not guarantee that it will always follow every instruction.

## 6. What is Temperature?

Simple Meaning (Hinglish):

Temperature model ke output ki randomness ko influence karta hai.

Tumhare code mein:

```
const ai = new ChatGoogleGenerativeAI({
    model: "gemini-3.7-flash",
    apiKey: process.env.GEMINI_API_KEY,
    temperature: 1,
    maxOutputTokens: 570
});
```

- Lower temperature generally more predictable outputs ko encourage karta hai.
- Higher temperature generally more varied outputs ko encourage karta hai.
- `maxOutputTokens` generated response ki maximum token limit set karta hai, subject to provider support.

Interview-ready answer (English):

Temperature is a model-generation parameter that influences the randomness of token selection. Lower values generally produce more predictable responses, while higher values can produce more diverse responses. Its exact effect depends on the model implementation.

When should you use it?

| Use case         | Typical approach                                 |
| ---------------- | ------------------------------------------------ |
| Factual Q&A      | Lower temperature                                |
| Code generation  | Lower temperature is often a good starting point |
| Creative writing | Higher temperature may be useful                 |
| Brainstorming    | Experiment with moderate or higher values        |

These are starting points, not universal rules. Temperature does not guarantee factual accuracy.

## 7. How to Build a Chat API Using Express and LangChain

Simple Meaning (Hinglish):

Hum Express server banayenge jisme `/chat` endpoint user se prompt receive karega, LangChain ke through AI model ko call karega, aur response JSON mein return karega.

### Application flow

Thunder Client / Frontend

POST /chat with a JSON prompt

Express Server

Parse JSON and validate prompt

LangChain Chat Model

invoke() → AI response

JSON Response