
const express = require("express");
const dotenv = require("dotenv");

// Load environment variables from the .env file
dotenv.config();

// Create the Express application
const app = express();

// Allow Express to read JSON request bodies
app.use(express.json());

async function main() {
    // Import LangChain's universal chat model initializer
    const { initChatModel } = await import(
        "langchain/chat_models/universal"
    );

    // Check whether the Gemini API key exists
    if (!process.env.GEMINI_API_KEY) {
        throw new Error("GEMINI_API_KEY is missing in .env");
    }

    // Set the environment variable expected by the Google provider
    process.env.GOOGLE_API_KEY = process.env.GEMINI_API_KEY;

    // Initialize the Gemini chat model through LangChain
    const model = await initChatModel(
        "google:gemini-3.8-flash"
    );

    // Home route to check whether the server is running
    app.get("/", (req, res) => {
        res.send("Hello! LangChain server is running.");
    });

    // API route for sending prompts to Gemini
    app.post("/chat", async (req, res) => {
        try {
            // Get the prompt from the incoming JSON body
            const { prompt } = req.body;

            // Validate the prompt before calling the model
            if (typeof prompt !== "string" || !prompt.trim()) {
                return res.status(400).json({
                    error: "A valid prompt is required"
                });
            }

            // Send the prompt to Gemini using LangChain
            const result = await model.invoke(prompt);

            // Print the AI response in the terminal
            console.log(result.text);

            // Send the AI response back to the client
            return res.json({
                response: result.text
            });

        } catch (error) {
            // Log the actual error for debugging
            console.error("LangChain error:", error);

            // Return a safe error message to the client
            return res.status(500).json({
                error: "Failed to generate AI response"
            });
        }
    });

    // Read the port from .env or use 9091 as the default
    const PORT = process.env.PORT || 9091;

    // Start the Express server
    app.listen(PORT, () => {
        console.log(`Server is running at http://localhost:${PORT}`);
    });
}

// Start the application and handle startup errors
main().catch((error) => {
    console.error("Server startup error:", error.message);
    process.exit(1);
});
