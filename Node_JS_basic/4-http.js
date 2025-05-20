// Étape 1: Importer le module HTTP
import http from 'http';

// Étape 2: Créer le serveur
const app = http.createServer((req, res) => {
    // À chaque requête vers le serveur, ce code sera exécuté

    res.write('Hello Holberton School!'); // On définit le statut HTTP et les en-têtes de la réponse
    res.end(); // On envoie une réponse au client
});

// Étape 3: Démarrer le serveur
app.listen(1245)
module.exports = app;
