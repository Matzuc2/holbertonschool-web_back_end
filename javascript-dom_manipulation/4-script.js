document.getElementById("add_item").onclick = function() {
    const ul = document.querySelector("ul.my_list");
    const li = document.createElement("li");
    const Item = "Item";
    li.textContent = Item;
    ul.appendChild(li);
}