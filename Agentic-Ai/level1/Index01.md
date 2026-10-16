
## 1. Important concepts

### 1. Express.js

Express.js is a web framework for Node.js. It helps us create servers and APIs.

```
const express = require("express");
const app = express();
```

- `require("express")` imports Express.
- `express()` creates an Express application.

### 2. dotenv

Dotenv loads environment variables from a `.env` file.

```
const dotenv = require("dotenv");
dotenv.config();
```

Example `.env` file:

```
PORT=9890
GEMINI_API_KEY=your_api_key
```

### 3. `process.env.PORT`

Reads the port number from the environment.

```
const PORT = process.env.PORT || 9890;
```

If `PORT` exists, use it. Otherwise, use `9890`.

### 4. Dynamic `import()`

You are using CommonJS with `require()`, so dynamic `import()` lets you load the Gemini SDK without changing your entire project to ES Modules.

```
const { GoogleGenAI } = await import("@google/genai");
```

This statement must be inside an `async` function in your current setup.

### 5. GoogleGenAI

Used to create a client for calling Google's Generative AI SDK.

```
const ai = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY
});
```

Keep your API key private.

## 2. Normal response vs. streaming response

### Normal response

Send prompt

Wait for complete answer

Receive answer

The application waits for the complete response before using it.

### Streaming response

Send prompt

Receive events as they arrive

Process each event

The application can process response events as they arrive instead of waiting for the entire answer.

## 3. How to create a normal response

```
const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain AI in simple words"
});

console.log(interaction.output_text);
```

- `ai.interactions.create()` sends a request to the AI API.
- `model` specifies the model to use.
- `input` contains your prompt.
- `await` waits for the API operation to complete.
- `output_text` contains the generated text.

## 4. How to stream a response

```
const stream = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works",
    stream: true
});

for await (const event of stream) {
    console.log(event);
}
```

Important terms:

- `stream: true` requests a streamed response.
- `for await...of` processes items from an asynchronous iterable one at a time.
- `event` represents an event emitted by the stream.
- `console.log(event)` prints each event in the terminal.

The stream can contain different event types, such as text deltas and completion events. You should inspect the event type and data to extract only the text you want.

## 5. Why do we use `async/await`?

An API call can take time to return a result. `async/await` makes it easier to write code that waits for asynchronous operations.

```
async function main() {
    const result = await someAsyncFunction();
    console.log(result);
}

main().catch(console.error);
```

- `async` defines an asynchronous function.
- `await` waits for a Promise to settle.
- `.catch(console.error)` handles a rejected Promise from `main()`.

## 6. What is `app.listen()`?

```
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

It starts the Express server and listens on the selected port. The callback runs when the server starts listening.

Remember: In your current script, the Gemini stream runs in the terminal. To stream the response to a browser, you need to place the streaming logic inside an Express route and send the events to the client.

## 7. Interview questions and answers

Q1. What is streaming in AI?

Streaming means receiving and processing a response in parts as it becomes available.

Q2. What is the difference between a normal response and a streaming response?

A normal response is returned as a complete result, while streaming allows us to process events as they arrive.

Q3. What is `for await...of`?

It is a loop used to process values from an asynchronous iterable one at a time.

Q4. Why do we use `async`?

We use `async` to define a function that can perform asynchronous operations with `await`.

Q5. Why do we use `try/catch`?

We use `try/catch` to handle errors that may happen during API calls or other operations.

Q6. Why do we use `.env`?

We use `.env` to store configuration values and secrets outside the source code.

Q7. What is an API key?

An API key is a credential used to identify or authorize an application when accessing an API.

## 8. Quick revision table

| Concept            | Purpose                            |
| ------------------ | ---------------------------------- |
| Express.js         | Build servers and APIs             |
| `dotenv.config()`  | Load environment variables         |
| `process.env.PORT` | Read the port setting              |
| `GoogleGenAI`      | Create the Google AI client        |
| `async/await`      | Handle asynchronous operations     |
| `stream: true`     | Request streamed output            |
| `for await...of`   | Process asynchronous stream events |
| `output_text`      | Access the complete generated text |
| `app.listen()`     | Start the Express server           |

```