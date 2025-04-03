document.getElementById("toggle_header").onclick = function() {
    const h = document.querySelector("header")
    if (h.className == "red"){
        h.className = "green"
    }
    else if(h.className == "green"){
        h.className = "red"
    }
}