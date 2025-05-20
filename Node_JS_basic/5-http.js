const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  // À chaque requête vers le serveur, ce code sera exécuté
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    if (process.argv[2]) {
      countStudents(process.argv[2])
        .then((data) => {
          res.writeHead(200, { 'Content-Type': 'text/plain' })
          res.end(`This is the list of our students\n${data}`);
        })
        .catch((error) => {
          res.writeHead(200, { 'Content-Type': 'text/plain' })
          res.end(`This is the list of our students\n${error.message}`);
        });
    } else {
      res.end('This is the list of our students\nCannot load the database');
    }
  }
});

// Démarrer le serveur
app.listen(1245);
module.exports = app;
