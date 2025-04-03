const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
async function SaleChien() {
	const response = await fetch(url);
	const data = await response.json();
	let h = document.getElementById("character");
	h.innerHTML = data.name;
}
SaleChien();
