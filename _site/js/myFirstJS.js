
function myFunction() {
    var x = document.getElementById("landingTopNav")
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";    
    }
}

function toggleHam(x) {
    x.classList.toggle("change");
}


