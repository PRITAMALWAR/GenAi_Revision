
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













const express = require("express");

const app = express();

app.get("/", (req, res) => {
    res.send("Hello! Express server is running.");
});


const PORT = 8809
app.listen(PORT, () => {
    console.log(`Server running at ${PORT}`);
});
