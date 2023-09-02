// archivo: static/js/agenda.js

document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendario');
    const calendar = new FullCalendar.Calendar(calendarEl, {
      selectable: true, // Permite selección de fechas
      select: function(info) {
        // La función se ejecuta cuando el usuario selecciona una fecha/hora
        const fechaInicio = info.startStr;
        const fechaFin = info.endStr;
  
        // Aquí puedes almacenar la información en un formulario oculto
        document.getElementById('id_fecha_inicio').value = fechaInicio;
        document.getElementById('id_fecha_fin').value = fechaFin;
      },
      // Otras opciones y personalización según tus necesidades
    });
    calendar.render();
  });