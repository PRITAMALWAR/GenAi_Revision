## 1. Basic Node.js Interview Questions

Q1. What is Node.js?

Interview answer

Node.js is a JavaScript runtime environment. It allows us to run JavaScript outside the browser, mainly on the server.

Q2. What is a server?

A server is a program that receives requests from clients and sends responses back.

Q3. What is npm?

npm stands for Node Package Manager. It helps us install and manage packages in a Node.js project.

Q4. What is `npm init -y`?

It creates a `package.json` file with default settings without asking questions.

Q5. What is `package.json`?

It stores project information, dependencies, and scripts.

## 2. Express.js Interview Questions

Q6. What is Express.js?

Express.js is a web framework for Node.js. It makes it easier to create servers and APIs.

Q7. Why do we use Express.js?

We use Express.js to handle requests, create routes, and send responses easily.

Q8. How do you install Express.js?

We install it using this command:

```
npm install express
```

Q9. What is `app.get()`?

`app.get()` handles GET requests for a specific route.

Example:

```
app.get("/", (req, res) => {
    res.send("Hello World");
});
```

Q10. What are `req` and `res`?

- `req` means request. It contains information sent by the client.
- `res` means response. We use it to send data back to the client.

Q11. What is `app.listen()`?

It starts the server and makes it listen for requests on a specified port.

## 3. Environment Variables and dotenv

Q12. What is dotenv?

Dotenv is a package that loads environment variables from a `.env` file into `process.env`.

Q13. Why do we use a `.env` file?

We use it to store configuration values, such as the port number and database URL. It can also store secrets, which should never be committed to Git.

Q14. How do you use dotenv?

First, install it:

```
npm install dotenv
```

Then write this in `index.js`:

```
require("dotenv").config();
```

Q15. What is `process.env.PORT`?

It reads the `PORT` environment variable from the Node.js environment.

Q16. Why do we write `process.env.PORT || 8809`?

It uses the environment-provided port if available. Otherwise, it uses `8809` as the default port.

## 4. URL, localhost and port

Q17. What is a URL?

URL stands for Uniform Resource Locator. It is the address used to access a resource.

Q18. What is localhost?

Localhost refers to our own computer. We use it to test applications locally.

Q19. What is a port?

A port is a number used to direct network traffic to a service on a computer.

Q20. What is the difference between localhost and a port?

Localhost identifies the computer, while the port identifies the service endpoint on that computer.

Example: `http://localhost:8809`

- `http` — protocol
- `localhost` — your computer
- `8809` — port number

## 5. Important code for interviews

This is the basic Express server you have learned so far.

```

const express = require("express");
require("dotenv").config();

const app = express();

app.get("/", (req, res) => {
    res.send("Hello! Express server is running.");
});

const PORT = process.env.PORT || 8809;

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

```

