# AI Agents — Complete Notes

Hinglish explanation same format mein rakhenge, with interview-ready English answers, practical examples, LangChain code, and important concepts based on your screenshots.

## 1. What is an AI Agent?

Simple Meaning (Hinglish):

An AI Agent ek aisa system hai jo AI model ka use karke decide karta hai ki kisi goal ko complete karne ke liye kaun-se actions lene chahiye.

Ek normal LLM user ke input ko samajhkar response generate karta hai. AI Agent LLM ke saath tools use karke actions bhi perform kar sakta hai.

An agent can:

- Understand a goal
- Make decisions
- Select tools
- Execute actions
- Observe results
- Change its next action
- Stop when the task is complete

Example:

```
User:
"Meri sales check karke report email karo."

        ↓

    AI Agent
        ↓
  Database Tool
        ↓
   Sales Data
        ↓
  Generate Report
        ↓
    Email Tool
        ↓
   Report Sent
```

Interview-ready answer (English):

An AI agent is a system that uses an AI model to determine and execute actions toward achieving a goal. Depending on its design, it can select tools, observe tool results, make further decisions, and stop when the task is completed or a stopping condition is reached.

## 2. LLM vs AI Agent

| LLM                                                | AI Agent                                               |
| -------------------------------------------------- | ------------------------------------------------------ |
| Input ko process karke response generate karta hai | Goal complete karne ke liye actions bhi le sakta hai   |
| Normally model response generate karta hai         | Model, tools aur control flow ko combine kar sakta hai |
| Tool execution ke bina answer de sakta hai         | Tools use kar sakta hai when needed                    |
| Example: Explain JWT                               | Example: Check data, generate report, send email       |

Example 1 — LLM:

```
User: "Explain JWT"

LLM → JWT explain karega
```

Example 2 — AI Agent:

```
User: "Meri sales report banao aur email karo"

Agent → Database check karega
       → Report generate karega
       → Email tool use karega
       → Task status report karega
```

Interview-ready answer (English):

An LLM is a model that processes input and generates output. An AI agent is a broader system that uses an LLM or another decision-making mechanism, together with tools and control logic, to accomplish goals through actions.

Important: Har AI agent ko fully autonomous hona zaroori nahi hai. Agent ki autonomy uski implementation aur permissions par depend karti hai.

## 3. What is a Tool?

Simple Meaning (Hinglish):

Tool ek function ya capability hai jo AI Agent ko koi action perform karne ya external information access karne mein help karta hai.

LLM powerful hai, lekin uske paas automatically har external system ka access nahi hota. Tools ke through hum model ko APIs, databases, search systems aur apne application functions ke saath connect kar sakte hain.

Example: Current Weather

User

"What is the current weather in Delhi?"

LLM

Decides that current weather data is needed

Weather Tool → Weather API

Fetches the current conditions

LLM

Uses the returned data to formulate an answer

Interview-ready answer (English):

A tool is a function or interface that allows an AI agent to perform a defined operation or access external information. Examples include web search, database queries, weather APIs, and sending emails. A model can request a tool call, while the application or agent runtime executes it and returns the result.

## 4. Types of Tools

Your screenshot divides tools into two main categories.

[Instinct Academy](https://images.openai.com/static-rsc-4/AFp8lvruNZ1-wogV0Db3SKhJ8L-YIkCztOEpUecfScUjgTZMJO7h-jHrbA8OGqSV8niNCxgGO8TJdq60speOW6yfavfo2RbiEYh4qdMX5ZfoMvYX5447Xnk_OJ-uj_050zy_j_0nJkdiI-WF1p3PtGzAgawsHzaY4IxFKucxyx8?purpose=inline)

1\. Built-in / Utility Tools

Ready-made tools or integrations that provide common capabilities.

Examples:

- Web search
- Calculator
- Weather API integration
- Supported database or retrieval integrations

Example: Tavily Search can retrieve relevant web results when properly configured.

[Frontend Developer Interview AI: How to Actually Prepare in 2026 - AceRound Blog](https://images.openai.com/static-rsc-4/xGo8cyenI2bvzxaBEqkHa8FG_3_H_Vzp3foaUSNl35EQoZkqKTBZZdOE6m0gzDy64qTo-QuUNhVFmMcyiPBCAuOz6Ajq9RzH6-NHbP-po9CZ7CLYfxoBUTtRCraY834TpCrrJruqpJZtI2aE4ZMaY3RvVLCJjeTHewVcqWQf3fc?purpose=inline)

2\. Custom Tools

Apne application ki requirement ke according khud tool define karna.

Examples:

- `search_database`
- `get_sales_report`
- `get_weather`
- `send_email`

Example: Company ke customer database mein records search karne ke liye custom tool.

Interview-ready answer (English):

Tools can be existing integrations or custom functions. Existing integrations provide reusable capabilities, while custom tools expose application-specific operations through defined inputs and outputs.

## 5. What is a Custom Tool?

Simple Meaning (Hinglish):

Maan lo tumhare application mein customer database hai. Tum chahte ho ki AI Agent user ke question ke according database search kare.

Iske liye tum `search_database` naam ka custom tool bana sakte ho.

Screenshot ka example:

```
import * as z from "zod";
import { tool } from "langchain";

const searchDatabase = tool(
    async ({ query, limit }) => {
        // Demo result; replace with a real database query
        return `Found up to ${limit} results for "${query}"`;
    },
    {
        name: "search_database",
        description:
            "Search the customer database for records matching the query.",
        schema: z.object({
            query: z.string().describe(
                "Search terms to look for"
            ),
            limit: z.number().describe(
                "Maximum number of results to return"
            )
        })
    }
);
```

This is a demonstration tool. It does not connect to a real database until you implement the database query inside the function.

### Code ka breakdown

| Code                               | Meaning                                                    |
| ---------------------------------- | ---------------------------------------------------------- |
| `import * as z from "zod"`         | Input schema define aur validate karne ke liye             |
| `import { tool } from "langchain"` | LangChain tool abstraction import karna                    |
| `async ({ query, limit }) => ...`  | Tool execute hone par chalne wala function                 |
| `name`                             | Tool ka unique identifier                                  |
| `description`                      | Model ko batata hai tool kab use karna useful ho sakta hai |
| `schema`                           | Tool ke expected input ka structure define karta hai       |

### What is Zod?

Simple Meaning (Hinglish): Zod ek TypeScript-friendly schema validation library hai. Iska use data ke expected structure aur types define karne ke liye hota hai.

Example:

```
const schema = z.object({
    query: z.string(),
    limit: z.number()
});
```

Is schema ke according `query` string aur `limit` number hona chahiye.

Interview-ready answer (English):

A custom tool is an application-defined function exposed to an AI model through a tool interface. Its name, description, and input schema help the model determine when to request it and what arguments to provide. The application executes the function and returns its result.

## 6. How Does an AI Agent Use a Tool?

Simple Meaning (Hinglish):

Agent har question par tool use nahi karta. Woh question ko analyze karta hai aur decide karta hai ki available tools mein se kisi tool ki zarurat hai ya nahi.

Typical flow:

```
User Query
    ↓
LLM / Agent
    ↓
Analyze the Goal
    ↓
Select a Tool (if needed)
    ↓
Execute Tool
    ↓
Receive Tool Result
    ↓
LLM Processes the Result
    ↓
Final Response
```

Example:

User: `"Find customer Rahul in the database."`

1. Agent user ka goal samjhega.
2. `search_database` tool select kar sakta hai.
3. Tool ko required query pass hogi.
4. Application database query execute karegi.
5. Tool matching records return karega.
6. Agent result ko user-friendly response mein explain karega.

Important: Tool select karna aur execute karna alag steps hain. Model tool call request kar sakta hai, lekin execution LangChain runtime aur application ke through hota hai.

Interview-ready answer (English):

An agent typically follows a tool-calling cycle: it interprets the user's request, decides whether a tool is needed, generates a structured tool call, executes the tool through its runtime, observes the result, and generates a response or takes another action.

## 7. Build an AI Agent Using Simple LangChain

Your screenshot shows two approaches for building AI agents:

[LangChain (@LangChain) on X](https://images.openai.com/static-rsc-4/2mxJeCG-inAklnQu8SSJbr1XikpC86lXuW6Ixu01j9YrgzBmAYL_6H4-Bj6Kb67RGwYxw1aQlkHw09bSjRLKT0vBwMYAv-Qai-By02fOHVBjIE5Um_5vRq5ulrb6PfN9oOedr1kCHW8O30DJX-6mzZ7L-Ie0StGtXsIOC9V1nPM?purpose=inline)

Approach 1: Agent with simple LangChain

Use a higher-level agent API such as `createAgent()`.

Best starting point for a tool-using assistant with a straightforward workflow.

[Agentic AI: Building Intelligent Workflows \[Guide\] | Scalable Path](https://images.openai.com/static-rsc-4/MhIVUGBTD6cthfiENCrhftYT4kimx9rNOhLSiHXfHY01GMaTs8fc70iD4XkfLW4fkJgYCuE2c6mZf_KHdaGSpIyq9hlmkfeMvxKED-bNKcJKcX-gyIQH9ouy9sbYIewJTGxMGGhHoGgY5aEDuDptUuOrwmLb8REOBNfMtdUlQIE?purpose=inline)

Approach 2: Agent with LangGraph

Use graph-based workflow orchestration.

Useful when you need explicit control over state, branching, loops, checkpoints, or human approval.

### Complete example: Custom tool + Gemini agent

Install the dependencies:

```
npm install langchain @langchain/google-genai zod dotenv
```

Set the API key in `.env`:

```
GEMINI_API_KEY=your_actual_gemini_api_key
```

Create `agent.js`:

```
import "dotenv/config";
import { createAgent, tool } from "langchain";
import { z } from "zod";

// 1. Define a custom tool
const searchDatabase = tool(
    async ({ query, limit }) => {
        // Demo implementation.
        // Replace this with a real database query.
        return JSON.stringify({
            query,
            limit,
            records: [
                { name: "Rahul", department: "Engineering" }
            ]
        });
    },
    {
        name: "search_database",
        description:
            "Search customer records using a query and result limit.",
        schema: z.object({
            query: z.string().describe(
                "Customer name or search terms"
            ),
            limit: z.number().int().min(1).max(20).describe(
                "Maximum number of records"
            )
        })
    }
);

// 2. Create the agent
const agent = createAgent({
    model: "google:gemini-3.5-flash",
    tools: [searchDatabase],
    systemPrompt:
        "You are Jarvis, a helpful assistant. Use the database tool when customer records are needed."
});

// 3. Invoke the agent
const result = await agent.invoke({
    messages: [
        {
            role: "user",
            content: "Find Rahul in the customer database."
        }
    ]
});

// 4. Read the final message
const messages = result.messages;
console.log(messages[messages.length - 1].content);
```

Before running this example, verify that your installed LangChain and Google integration versions support the shown configuration and that `google:gemini-3.5-flash` is available to your account. Replace the demo tool with a real database implementation for production.

### Code ka breakdown

1. `tool()` — custom function ko tool interface mein convert karta hai.
2. `z.object()` — tool ke input fields define karta hai.
3. `createAgent()` — model aur tools ko agent ke roop mein configure karta hai.
4. `agent.invoke()` — agent workflow ko start karta hai.
5. `result.messages` — workflow ke messages aur final response access karne deta hai.

Interview-ready answer (English):

LangChain's `createAgent()` provides a higher-level interface for building agents that use a language model and tools. The model can request tool calls, and the agent runtime handles their execution and passes the results back to the model.

## 8. What is LangGraph?

Simple Meaning (Hinglish):

LangGraph ek framework hai jo AI agent workflows ko graph ke form mein define karne deta hai. Isme nodes tasks perform karte hain aur edges decide karte hain ki next execution kahan jayega.

Example: Sales Report Agent

```
        START
          ↓
     Understand Goal
          ↓
     Fetch Sales Data
          ↓
     Analyze Results
          ↓
     Generate Report
          ↓
    Approval Required?
       ↙       ↘
      Yes       No
       ↓         ↓
    Approval   Finish
       ↓
    Send Report
       ↓
      END
```

Is tarah ke workflows mein branching, retries, state management, checkpoints aur human approval jaise features useful hote hain.

Interview-ready answer (English):

LangGraph is a framework for building stateful, graph-based AI workflows. It allows developers to define nodes, transitions, conditional routing, and state management for workflows that may involve multiple model calls, tool executions, or human intervention.

### LangChain Agent vs LangGraph

| Simple LangChain agent                    | LangGraph                                                 |
| ----------------------------------------- | --------------------------------------------------------- |
| High-level agent abstraction              | Graph-based workflow orchestration                        |
| Common agent workflows ke liye convenient | Complex workflows par detailed control                    |
| Model aur tools configure karna easy      | Nodes, edges, state aur transitions define kar sakte hain |
| Less explicit workflow control            | Explicit workflow control and branching                   |

Important: Dono mutually exclusive nahi hain. Modern LangChain agents graph-based execution infrastructure use kar sakte hain, aur LangGraph ko custom workflows banane ke liye directly bhi use kiya ja sakta hai.

## 9. Express + AI Agent — Application Architecture

Tumhare VS Code screenshot mein Express server ka basic setup dikhaya gaya hai.

```
import express from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();

// Parse incoming JSON
app.use(express.json());

// Configure the server port
const port = process.env.PORT || 5000;

// Home route
app.get("/", (req, res) => {
    res.send("AI Agent server is running");
});

// Start the server
app.listen(port, () => {
    console.log("Server started at", port);
});
```

Simple Meaning (Hinglish):

- `express()` application create karta hai.
- `dotenv.config()` environment variables load karta hai.
- `express.json()` incoming JSON request body parse karta hai.
- `app.get()` HTTP GET endpoint define karta hai.
- `app.listen()` server start karta hai.

Run karne se pehle ensure karo ki project ESM support karta hai, for example `package.json` mein `"type": "module"` ho.

### Agent ko API endpoint se connect karna

```
app.post("/agent", async (req, res) => {
    try {
        const { prompt } = req.body;

        if (typeof prompt !== "string" || !prompt.trim()) {
            return res.status(400).json({
                error: "A valid prompt is required"
            });
        }

        const result = await agent.invoke({
            messages: [
                {
                    role: "user",
                    content: prompt
                }
            ]
        });

        const messages = result.messages;
        const finalMessage = messages[messages.length - 1];

        return res.json({
            response: finalMessage.content
        });

    } catch (error) {
        console.error("Agent error:", error);

        return res.status(500).json({
            error: "Agent execution failed"
        });
    }
});
```

Yeh route upar define kiye gaye `agent` instance ko use karta hai. Isko same application mein, `app.listen()` call se pehle add karna hai.

Production note: Real applications mein authentication, rate limits, request timeouts, logging, and tool permissions bhi configure karne chahiye.

## 10. Interview Questions — AI Agents

1\. What is an AI agent?

2\. What is a tool in AI agents?

3\. Why do we need tools?

4\. What is a custom tool?

5\. Why do we use Zod?

6\. What is tool calling?

7\. What is createAgent()?

8\. What is LangGraph?

9\. Can an LLM alone access a live database?

10\. What is the difference between an AI agent and a normal chatbot?

## Final Revision — AI Agent Workflow

1\. User Goal

User defines the task

2\. LLM / Agent

Understand and decide

3\. Tool Selection

Choose an available tool if needed

4\. Tool Execution

Call API, database, or function

5\. Observe Result

Evaluate returned information

6\. Final Response
