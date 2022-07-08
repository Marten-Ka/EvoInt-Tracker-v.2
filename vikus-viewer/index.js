
const express = require('express');
const app = express();
const http = require('http');
const fs = require('fs');
const port = 8080;

app.use(express.static(__dirname));

app.get('/vikus_viewer', (_, res) => {
    const html = fs.readFileSync("./index.html", "utf8")
    res.send(html);
})

// Create the server and listen on port
http.createServer(app).listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});