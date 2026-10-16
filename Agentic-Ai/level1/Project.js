
const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.use(express.json());

async function main() {
    const { GoogleGenAI } = await import("@google/genai");

    const ai = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY
    });

    // Home route
    app.get("/", (req, res) => {
        res.send("Hello! Express server is running.");
    });

    // Chat API
    app.post("/chat", async (req, res) => {
        try {
            const { prompt } = req.body;

            if (!prompt) {
                return res.status(400).json({
                    error: "Prompt is required"
                });
            }

            const result = await ai.models.generateContent({
                model: "gemini-2.5-flash",
                contents: prompt
            });

            return res.json({
                response: result.text
            });
        } catch (error) {
            console.error("Gemini API error:", error.message);

            return res.status(500).json({
                error: "Failed to generate AI response"
            });
        }
    });

    const PORT = process.env.PORT || 9890;

    app.listen(PORT, () => {
        console.log(`Server is running at http://localhost:${PORT}`);
    });
}

main().catch(console.error);
