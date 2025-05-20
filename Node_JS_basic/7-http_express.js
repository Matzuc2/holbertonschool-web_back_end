// Import Express
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.use(express.text());
// Define a route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    });
});
// Start the server
app.listen(1245);
