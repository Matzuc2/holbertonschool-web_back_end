const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
// À chaque requête vers le serveur, ce code sera exécuté

  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.write('Hello Holberton School!')
    res.end(); // On envoie une réponse au clien
  }
  else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' }); // On définit le statut HTTP et les en-têtes de la réponse
    res.write("This is the list of our students\n")
    res.write(countStudents('./database.csv'))
    res.end()
  }
});
// Étape 3: Démarrer le serve
app.listen(1245);
module.exports = app;