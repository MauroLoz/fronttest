// Funcion dropdown navbar

document.addEventListener("DOMContentLoaded", function() {
    var profileImg = document.getElementById("profile-img");
    var dropdown = document.getElementById("dropdown");
    
    profileImg.addEventListener("click", function() {
        if (dropdown.style.display === "block") {
            dropdown.style.display = "none";
        } else {
            dropdown.style.display = "block";
        }
    });
    
    // Cerrar el menú desplegable si se hace clic en cualquier parte fuera de él
    window.addEventListener("click", function(event) {
        if (event.target != profileImg && event.target != dropdown) {
            dropdown.style.display = "none";
        }
    });
});
