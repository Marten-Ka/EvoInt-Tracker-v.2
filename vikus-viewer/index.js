
const express = require('express');
const app = express();
const http = require('http');
const path = require('path');
const fs = require('fs');
const port = 8080;
// Use the whole root as static files to be able to serve the html file and
// the build folder

app.use("/vikus-viewer",express.static(path.join(__dirname, '/')));
// Send html on '/'path



app.get('/vikus', (req, res) => {
    const html = fs.readFileSync("./html.html", "utf8")
    res.send(html);
})

// Create the server and listen on port
http.createServer(app).listen(port, () => {
    console.log(`Server running on localhost:${port}`);
});