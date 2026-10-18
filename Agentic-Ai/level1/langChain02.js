
const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.use(express.json());

async function main() {
    // Import LangChain Google Chat Model
    const { ChatGoogleGenerativeAI } = await import(
        "@langchain/google-genai"
    );

    // Create Gemini model
    const ai = new ChatGoogleGenerativeAI({
        model: "gemini-3.7-flash",
        apiKey: process.env.GEMINI_API_KEY,
        temperature:1,
        maxOutputTokens:570
    });

    // Home route
    app.get("/", (req, res) => {
        res.send("LangChain server is running");
    });

    // Chat API
    app.post("/chat", async (req, res) => {
        try {
            const { prompt } = req.body;

            // Validate prompt
            if (typeof prompt !== "string" || !prompt.trim()) {
                return res.status(400).json({
                    error: "Prompt is required"
                });
            }

            // Send system and human messages to Gemini
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

            // Return AI response
            return res.json({
                response: result.content
            });

        } catch (error) {
            console.error("LangChain error:", error.message);

            return res.status(500).json({
                error: "Failed to generate AI response"
            });
        }
    });

    // Start server
    const PORT = process.env.PORT || 9091;

    app.listen(PORT, () => {
        console.log(`Server running at http://localhost:${PORT}`);
    });
}

main().catch(console.error);
