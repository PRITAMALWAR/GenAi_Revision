
const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.use(express.json());

async function main() {
    // Import LangChain's Groq chat model
    const { ChatGroq } = await import("@langchain/groq");

    // Check whether the Groq API key exists
    if (!process.env.GROQ_API_KEY) {
        throw new Error("GROQ_API_KEY is missing in .env");
    }

    // Create the Groq AI model
    const ai = new ChatGroq({
        model: "openai/gpt-oss-120b",
        apiKey: process.env.GROQ_API_KEY,
        temperature: 0.7
    });

    // Home route
    app.get("/", (req, res) => {
        res.send("Groq + LangChain server is running!");
    });

    // Chat API
    app.post("/chat", async (req, res) => {
        try {
            // Get the user's prompt
            const { prompt } = req.body;

            // Validate the prompt
            if (typeof prompt !== "string" || !prompt.trim()) {
                return res.status(400).json({
                    error: "Prompt is required"
                });
            }

            // Send system and human messages to Groq
            const result = await ai.invoke([
                {
                    role: "system",
                    content: "You are Jarvis, my personal AI assistant. Help me with programming and explain concepts in simple English."
                },
                {
                    role: "human",
                    content: prompt
                }
            ]);

            // Print the AI response in the terminal
            console.log(result.content);

            // Send the response to the client
            return res.json({
                response: result.content
            });

        } catch (error) {
            console.error("Groq API error:", error.message);

            return res.status(500).json({
                error: "Failed to generate AI response"
            });
        }
    });

    // Start the server
    const PORT = process.env.PORT || 9091;

    app.listen(PORT, () => {
        console.log(`Server running at http://localhost:${PORT}`);
    });
}

main().catch((error) => {
    console.error("Startup error:", error.message);
    process.exit(1);
});
