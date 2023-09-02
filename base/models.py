
# Definir y gestionar los modelos de base de datos 
from django.db import models

# Gestionar la autenticación y autorización de usuarios
from django.contrib.auth.models import User

# Trabajar con fechas y horas en Python.
from datetime import datetime

# Se definen los modelos de la base de datos para la aplicación específica


# Modelo asociado a los espacios
class Espacio(models.Model):
    # Título del espacio
    titulo = models.CharField(max_length=100)

    # Descripción del espacio
    descripcion = models.TextField()

    # Imágenes del espacio
    image1 = models.ImageField(upload_to='base/Images/EspaciosImages')
    image2 = models.ImageField(upload_to='base/Images/EspaciosImages')
    image3 = models.ImageField(upload_to='base/Images/EspaciosImages')

    # Tipo de combo
    tipoCombo=(
        ('Yoga', 'Yoga'),
        ('Arte', 'Arte'),
        ('Art.Marcial', 'Art.Marcial'),
        ('Cocina', 'Cocina'),
        ('Danza', 'Danza'),
        ('Musica', 'Musica'),
        ('Gimnasio', 'Gimnasio'),
        ('Fotografía', 'Fotografía'),
        ('Showroom', 'Showroom'),
        ('Otros', 'Otros'),
    )
    tipoEspacio = models.CharField(max_length=15, choices=tipoCombo)

    # Superficie del espacio
    superficie = models.IntegerField()

    # Características del espacio
    baño = models.BooleanField(default=False)
    estacionamiento = models.BooleanField(default=False)
    calefaccion = models.BooleanField(default=False)
    aire = models.BooleanField(default=False)
    techo = models.BooleanField(default=False)
    lineaTelefonica = models.BooleanField(default=False)
    agua = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

    # Dirección del espacio
    direccion = models.CharField(max_length=150)

    # Fecha de creación del espacio
    created = models.DateTimeField(auto_now_add = True)

    estadosPosibles = (
        ('EnEsperaAprobacion', 'EnEsperaAprobacion'),
        ('Publicado', 'Publicado'),
        ('Rechazado', 'Rechazado'),
    )
    estado = models.CharField(max_length=20, choices=estadosPosibles, default='EnEsperaAprobacion')

     # Relación con el usuario propietario del espacio
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Modelo asociado a los reservas de espacios
class Reserva(models.Model):
    post = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    nroCelular = models.IntegerField()
    fecha = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now)
    modos = (
        ('Efectivo en el Lugar', 'Efectivo en el Lugar'),
        ('Transferencia', 'Transferencia'),
    )
    tipoPago = models.CharField(max_length=30, choices=modos)
    estadosPosibles = (
        ('espera_aprobacion', 'Espera de Aprobación'),
        ('aprobada', 'Aprobada'),
        ('cancelada', 'Cancelada'),
        ('en_proceso', 'En Proceso'),
        ('finalizada', 'Finalizada'),
        ('pagada', 'Pagada'),
    )
    estado = models.CharField(max_length=20, choices=estadosPosibles, default='espera_aprobacion')


class ReseñaReserva(models.Model):
    puntaje_box=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    puntaje = models.IntegerField(choices=puntaje_box)
    text = models.TextField()
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


from django.db import models
from django.contrib.auth.models import User

class Espacio1(models.Model):
    nombre = models.CharField(max_length=100)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

class Disponibilidad(models.Model):
    espacio = models.ForeignKey(Espacio1, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)