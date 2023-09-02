
# Configurar y gestionar la interfaz de administración
from django.contrib import admin

# Se importan modelos Espacio y Reserva desde el archivo models.py.
from .models import Espacio, Reserva, ReseñaReserva, Espacio1, Disponibilidad, Event

# Registra el modelo Espacio y Reserva en la interfaz de administración
admin.site.register(Espacio)
admin.site.register(Reserva)
admin.site.register(ReseñaReserva)
admin.site.register(Espacio1)
admin.site.register(Disponibilidad)
admin.site.register(Event)