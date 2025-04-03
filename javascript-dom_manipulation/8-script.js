const url = "https://hellosalut.stefanbohacek.dev/?lang=fr"

async function NicolasSarkozy() {
    const FETCH = await fetch(url)
    const response = await FETCH.json();
    const DisBonjour = document.querySelector("#hello")
    DisBonjour.innerHTML = response.hello
}
NicolasSarkozy();