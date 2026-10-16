
```


index.js
Main server file — Express app, routes and server startup.


package.json
Project information, dependencies and npm scripts.


package-lock.json
Records the exact dependency versions selected by npm.


node_modules/
Installed packages, including Express and its dependencies.



```
require("express") — imports Express.
express() — creates the Express application.
app.get("/") — handles GET requests to the home route.
res.send() — sends a response to the client.
app.listen(3000) — starts the server on port 3000.

```