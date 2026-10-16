
// const http = require("http");

// const server = http.createServer((req, res) => {
//     res.writeHead(200, {
//         "Content-Type": "text/plain"
//     });

//     res.end("Hello! Node.js server is running.");
// });

// server.listen(3000, () => {
//     console.log("Server running at http://localhost:3000");
// });







// const express = require("express");
// const dotenv = require("dotenv");

// dotenv.config();

// const app = express();

// app.get("/", (req, res) => {
//     res.send("Hello! Express server is running.");
// });


// const PORT = process.env.PORT || 8809;

// app.listen(PORT, () => {
//     console.log(`Server running at http://localhost:${PORT}`);
// });














const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

app.get("/", (req, res) => {
    res.send("Hello! Express server is running.");
});

app.get("/ai", async (req, res) => {
    try {
        const { GoogleGenAI } = await import("@google/genai");

        const ai = new GoogleGenAI({
            apiKey: process.env.GEMINI_API_KEY
        });

        const interaction = await ai.interactions.create({
            model: "gemini-3.5-flash",
            input: "hello"
        });

        res.send(interaction.output_text);
        console.log(interaction.output_text)
    } catch (error) {
        console.error("Gemini API error:", error.message);
        res.status(500).send("Failed to get an AI response.");
    }
});

const PORT = process.env.PORT || 8809;

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
