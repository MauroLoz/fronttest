function changeStyle(){
    var x = document.getElementById("paginaForm");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

    var y = document.getElementById("myDiv2");
    y.style.display = "none";

    let btn = document.getElementById("value").value;
    let val = value.value;
    document.getElementById('paginaSection0Type').innerHTML = 'Salon para Yoga';

}

function changeStyle2(){
    var x = document.getElementById("paginaForm");  
    x.style.display = "none";
    

    var y = document.getElementById("myDiv2");
    y.style.display = "block";

}

function cambioEstadoDiv01(){
    var x = document.getElementById("seccion01div01");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function cambioEstadoDiv02(){
    var x = document.getElementById("seccion02div01");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function cambioEstadoDiv03(){
    var x = document.getElementById("seccion03div01");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function cambioEstadoDiv04(){
    var x = document.getElementById("seccion04div01");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function idDiv5(){
    var x = document.getElementById("iddiv-5");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}


function cambioEstadoDiv0sss1() {
    // Oculta el div actual de la sección 1
    document.getElementById('seccion01div01').style.display = 'none';
  }

  function mostrarSiguienteDisfsdv(id) {
    // Muestra el siguiente div pasando su ID como argumento
    document.getElementById(id).style.display = 'block';
  }


function mostrarSiguienteDiv(id) {
    document.getElementById(id).style.display = 'block';
}


