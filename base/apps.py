
# Definir opciones y ajustes específicos para la aplicación de forma personalizada.
from django.apps import AppConfig


class BaseConfig(AppConfig):
    # Configuración de la aplicación "base" 

    # Tipo de campo de clave primaria automática predeterminado
    default_auto_field = 'django.db.models.BigAutoField'

    # Nombre de la aplicación
    name = 'base'
