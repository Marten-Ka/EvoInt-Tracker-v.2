const express = require("express");
const { use } = require("express/lib/application");
const fs = require("fs")
const app = express();
const port = 3000;


app.get("/vikus-viewer", (req, res) => {
  res.sendFile(__dirname + "./vikus-viewer/index.html");
});




app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});