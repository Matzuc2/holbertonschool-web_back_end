// Import Express
const express = require('express');

const app = express();
// Define a route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
// Start the server
app.listen(1245);
module.exports = app;
