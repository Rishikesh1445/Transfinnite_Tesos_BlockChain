const { GoogleGenerativeAI } = require("@google/generative-ai"); // Import the module
const dotenv = require("dotenv"); // Import dotenv

dotenv.config(); // Load environment variables from .env file

const apiKey = process.env.API_KEY; // Your API key
const genAI = new GoogleGenerativeAI(apiKey);

async function generateContent(prompt) {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro-latest" });
    const result = await model.generateContent(prompt);
    console.log(result.response.text());
}

// Change the prompt here
generateContent("What are some interesting facts about generative AI?");
