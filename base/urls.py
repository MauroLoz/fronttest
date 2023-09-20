
# Definir las rutas de URL en una aplicación Django
from django.urls import path 

# Importa las vistas definidas en views.py
from . import views

# Configurar la entrega de archivos estáticos
from django.conf.urls.static import static

# Se importan las configuraciones globales de la aplicación Django.
from django.conf import settings


# Vamos a para definir las rutas de URL de la plataforma web, cada una asociada con su respectiva vista de comportamiento.

urlpatterns = [
    path('', views.home),
    path('login/', views.inicioSesion),
    path('logout/', views.cierreSesion),
    path('register/', views.register),
    path('nuevoespacio/', views.nuevoespacio),
    path('espacio/<int:id>', views.verespacio),
    path('verperfil/', views.verPerfil),
    path('reseña/', views.reseña),
    path('cambioEstadoAprobada/', views.cambioEstadoAprobada),
    path('cambioEstadoCancelada/', views.cambioEstadoCancelada),
    path('administrador/', views.administrador),
    path('cambioEspacioAprobado/', views.cambioEspacioAprobado),
    path('cambioEspacioCancelado/', views.cambioEspacioCancelado),
    path('calendario/', views.calendar_view, name='calendario'),
    path('hometest/', views.hometest),
    path('ver_agenda/<int:espacio_id>/', views.ver_agenda, name='ver_agenda'),
    path('base/', views.base),
    # path('calendar/', views.CalendarView.as_view(), name='calendar'),  # aquí
    path('calendar/<int:espacio_id>', views.CalendarView.as_view()),
    path('misEspacios/', views.misEspacios, name='misEspacios'),
    path('probando/', views.probando),

]


# Se utiliza para proporcionar acceso a los archivos de medios en el entorno de desarrollo de Django.

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)