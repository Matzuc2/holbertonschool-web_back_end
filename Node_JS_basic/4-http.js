const http = require('http');

const app = http.createServer((req, res) => {
// À chaque requête vers le serveur, ce code sera exécuté
  res.writeHead(200, { 'Content-Type': 'text/plain' }); // On définit le statut HTTP et les en-têtes de la réponse
  res.end('Hello Holberton School!'); // On envoie une réponse au client
});
// Étape 3: Démarrer le serve
app.listen(1245);
module.exports = app;
