
const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();

async function main() {
    const { GoogleGenAI } = await import("@google/genai");

    const ai = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY
    });

    // Default response
    // const interaction = await ai.interactions.create({
    //     model: "gemini-3.8-flash",
    //     input: "Tell me about the Samsung S26 Ultra in a few words",
    // });

    // console.log(interaction.output_text);


    // Stream the response
    const stream = await ai.interactions.create({
        model: "gemini-2.5-flash",
        input: "Explain how AI works",
        stream: true,
    });

    for await (const event of stream) {
        console.log(event);
    }
}

main().catch(console.error);

const PORT = process.env.PORT || 9890;

app.listen(PORT, () => {
    console.log(`Server is running on PORT ${PORT}`);
});
