


// simple way 




// import express from "express";
// import { ChatGoogle } from "@langchain/google";
// import dotenv from "dotenv";

// // 1. Configure environment variables
// dotenv.config();

// // 2. Initialize Express app
// const app = express();

// // 3. Middleware
// app.use(express.json());

// // 4. Initialize Gemini model
// const model = new ChatGoogle("gemini-3.8-flash");

// // 5. Test Gemini model
// const res = await model.invoke([
//   ["human", "hello"],
// ]);

// console.log(res.text);

// // 6. Configure port
// const port = process.env.PORT || 5000;

// // 7. Start server
// app.listen(port, () => {
//   console.log("server started at", port);
// });






// make post app



// import express from "express";
// import { ChatGoogle } from "@langchain/google";
// import dotenv from "dotenv";

// dotenv.config();

// const app = express();

// app.use(express.json());

// // Make a POST request
// app.post("/chat", async (req, res) => {
//   try {
//     const { prompt } = req.body;

//     const model = new ChatGoogle("gemini-3.8-flash");

//     const result = await model.invoke(prompt);
//     console.log(result.text)

//     return res.json({
//       response: result.text,
//     });
//   } catch (error) {
//     console.error("Gemini API Error:", error.message);

//     return res.status(500).json({
//       error: "Something went wrong",
//     });
//   }
// });




// const port = process.env.PORT || 5000;

// app.listen(port, () => {
//   console.log("server started at", port);
// });















import express from "express";
import { ChatGoogle } from "@langchain/google";
import { TavilySearch } from "@langchain/tavily";
import { createAgent } from "langchain";
import dotenv from "dotenv";

dotenv.config();

const app = express();

app.use(express.json());

// 1. Initialize Gemini LLM
const model = new ChatGoogle("gemini-3.8-flash");

// 2. Initialize Tavily Search Tool
const tool = new TavilySearch({
  maxResults: 5,
  topic: "general",
});

// 3. Create AI Agent = LLM + Tools
const agent = createAgent({
  model,
  tools: [tool],
});

// 4. Make a POST request
app.post("/chat", async (req, res) => {
  try {
    const { prompt } = req.body;

    if (!prompt) {
      return res.status(400).json({
        error: "Prompt is required",
      });
    }

    // 5. Invoke the agent
    const result = await agent.invoke({
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
    });

    // 6. Get the final answer
    const lastMessage = result.messages.at(-1);

    console.log(lastMessage.content);

    return res.json({
      response: lastMessage.content,
    });
  } catch (error) {
    console.error("Agent Error:", error);

    return res.status(500).json({
      error: "Something went wrong",
    });
  }
});

// 7. Start server
const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log("server started at", port);
});
