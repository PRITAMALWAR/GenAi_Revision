
const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.use(express.json());

async function main() {
    const { GoogleGenAI } = await import("@google/genai");

    if (!process.env.GEMINI_API_KEY) {
        throw new Error("GEMINI_API_KEY is missing in .env");
    }

    const ai = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY
    });

    app.get("/", (req, res) => {
        res.send("Hello! Express server is running.");
    });

    app.post("/chat", async (req, res) => {
        try {
            const { prompt } = req.body;

            const result = await ai.models.generateContent({
                model: "gemini-3.8-flash",
                contents: prompt
            });
            console.log(result.text)


            return res.json({
                response: result.text
            });
        } catch (error) {
            console.error("Gemini API error:", error);

            return res.status(500).json({
                error: "Failed to generate AI response"
            });
        }
    });

    const PORT = process.env.PORT || 9091;

    app.listen(PORT, () => {
        console.log(`Server is running at http://localhost:${PORT}`);
    });
}

main().catch((error) => {
    console.error("Server startup error:", error.message);
    process.exit(1);
});
