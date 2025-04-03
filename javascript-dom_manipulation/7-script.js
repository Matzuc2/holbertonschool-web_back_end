const url = "https://swapi-api.hbtn.io/api/films/";
async function fetchAvecTaMere() {
    const response = await fetch(url); //attendre réponse du fetch
    const data = await response.json(); // attendre retranscription json
    const ul = document.querySelector("ul#list_movies"); // Sélectionner tous les ul que j'encule.

    data.results.forEach(film => { // Parcourir tous les éléments de data.results et non pas DATA SEULEMENT 
        const li = document.createElement("li"); //créer nouvel élément (ligne dans liste)
        li.textContent = film.title; //"assigner à la ligne créée le titre du film 
        ul.appendChild(li); //ajouter ligne à chaque tour
    });
}
fetchAvecTaMere(); //appeler ta mère au téléphone avec la fonction