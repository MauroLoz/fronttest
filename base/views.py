
# Proteger una vista o función de vista en Django.
from django.contrib.auth.decorators import login_required

# Rendirzar una plantilla HTML y devolverla como respuesta HTTP
# Para redirigir a una URL específica
from django.shortcuts import render, redirect

# La implementación básica de un modelo de usuario en Django.
from django.contrib.auth.models import User

# Primero verificar las credenciales de un usuario en el sistema.
# Segundo se establece la sesión del usuario que ha iniciado sesión.
# Por ultimo para cerrar la sesión de un usuario.
from django.contrib.auth import authenticate, login, logout

# Almacenar mensajes temporales en la sesión del usuario.
from django.contrib import messages

# Se importan modelos Espacio y Reserva desde el archivo models.py.
from .models import Espacio, Reserva, ReseñaReserva

# Se importan los formularios espacioForm y reservaForm desde el archivo forms.py.
from .forms import espacioForm, reservaForm

# Realiza la paginación de conjuntos de datos en Django. 
from django.core.paginator import Paginator

# Importa la excepción Http404 del módulo django.http en Django.
from django.http import Http404

from django.http import HttpResponseRedirect



# Se definen las funciones de vista en python que manejan las solicitudes HTTP y generan las respuestas correspondientes.


from django.shortcuts import render
from .models import Espacio1, Disponibilidad

def ver_agenda(request, espacio_id):
    espacio = Espacio1.objects.get(pk=espacio_id)
    disponibilidades = Disponibilidad.objects.filter(espacio=espacio)
    
    return render(request, 'agenda.html', {'espacio': espacio, 'disponibilidades': disponibilidades})
def home(request): 
    # Obtiene el tipo de espacio del formulario enviado
    tipo = request.POST.get('tipo') 

    # Obtiene todos los objetos Espacio
    espacios2 = Espacio.objects.filter(estado = 'Publicado')

    # Obtiene el número de página actual (por defecto es 1)
    page = request.GET.get('page', 1) 

    # Filtra los espacios por el tipo especificado, si se proporciona
    if tipo:
        espacios2 = espacios2.filter(tipoEspacio = tipo)

    # Crea un objeto Paginator con 5 espacios por página
    paginator = Paginator(espacios2, 6) 

    # Obtiene la página actual de espacios
    espacios2 = paginator.page(page) 

    user = request.user

    # Prepara los datos a pasar a la plantilla 'home.html'
    data = {
        'entity':espacios2,
        'tipo': tipo,
        'paginator':paginator,
        'user': user
    }

    # Renderiza la plantilla 'home.html' con los datos proporcionados
    return render(request, 'home.html', data)

def inicioSesion(request):
    if(request.method == "POST"):
        # Obtener el nombre de usuario y la contraseña del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password) 

            if user is not None: 
                # Iniciar sesión y mostrar mensaje de éxito
                login(request, user) 
                messages.success(request, 'Se inicio Sesion correctamente')
                return redirect('/')
        
         # Mostrar mensaje de error si las credenciales son incorrectas
        messages.error(request, 'Datos incorrectos') 
    
    # Renderizar la plantilla de inicio de sesión
    return render(request, 'login.html') 

def cierreSesion(request):
    # Cierra la sesión actual del usuario y redigirige a la pagina de inicio 
    logout(request)
    return redirect('/')

def register(request):
    if (request.method == "POST"):
        # Obtener los datos del formulario de registro
        username = request.POST.get("username")
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if(password != confirm_password):
            # Mostrar mensaje de error si las contraseñas no coinciden
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')

        # Crear un nuevo usuario utilizando los datos proporcionados
        User.objects.create_user(username, first_name=name, last_name=lastname, password=password)

        # Redirigir al usuario a la página de inicio de sesión
        return redirect('/login/')
    
    # Renderizar la plantilla de registro
    return render(request, 'register.html')

@login_required
def nuevoespacio(request):
    if request.method == 'POST': 
        # Crear una instancia del formulario con los datos de la solicitud
        form_class = espacioForm(request.POST, request.FILES)

        if form_class.is_valid(): 
            # Guardar el espacio en la base de datos, asociándolo al usuario actual
            espacio = form_class.save(commit=False)
            espacio.user = request.user
            espacio.save()  

            # Mostrar mensaje de éxito y redirigir a la página principal
            messages.success(request, 'Espacio creado correctamente')
            return redirect('/')
    else:
        # Crear una instancia vacía del formulario
        form_class = espacioForm()

    # Renderizar la plantilla 'pagina.html' con el formulario
    return render(request, 'nuevoEspacio.html', {'form': form_class})

def verespacio(request, id = None):
        if request.method == 'POST':  
            # Crear una instancia del formulario con los datos de la solicitud       
            form = reservaForm(request.POST, request.FILES)

            if form.is_valid(): 
                # Obtener el objeto Espacio según el id proporcionado
                p = Espacio.objects.get(id = id)

                # Guardar la reserva en la base de datos, asociándola al usuario y al espacio correspondiente
                espacio = form.save(commit=False)
                espacio.user = request.user
                espacio.post = p
                espacio.save()  

                # Mostrar mensaje de éxito y redirigir a la página principal
                messages.success(request, 'Reserva creado correctamente')
                return redirect('/')

        context = {} 
        # Obtener el objeto Espacio según el id proporcionado
        p = Espacio.objects.get(id = id)

        form_class = reservaForm()
        # Agregar el objeto Espacio al contexto
        context = p

        # -----------------
        reseña = {} 
        cantidad = {} 
        c = ReseñaReserva.objects.filter(espacio = id)

        vueltas = 0
        contador = 0
        for x in c:
            vueltas += 1
            contador += x.puntaje
            reseña = int(contador) / int(vueltas)
            cantidad = int(vueltas)

        # -----------------

        # Renderizar la plantilla 'verespacio.html' con el contexto
        return render(request, 'verespacio.html', {'form': form_class,'espacio':context,'reseña':reseña,'cantidad':cantidad})

def verPerfil(request):
    context = {}

    if request.user.is_authenticated:
        # Obtener las reservas asociadas al usuario autenticado
        reservasEnEspera = Reserva.objects.filter(post__user = request.user).filter(estado = 'espera_aprobacion')
        reservasAprobadas = Reserva.objects.filter(post__user = request.user).filter(estado = 'aprobada')
        reservasRechazadas = Reserva.objects.filter(post__user = request.user).filter(estado = 'cancelada')

        # Agregar las reservas al contexto
        context['reservasEnEspera'] = reservasEnEspera
        context['reservasAprobadas'] = reservasAprobadas
        context['reservasRechazadas'] = reservasRechazadas

        # Renderizar la plantilla 'verPerfil.html' con el contexto
        return render(request, 'verPerfil.html', context)
    else:
        # Renderizar la plantilla 'login.html'
        return render(request, 'login.html')
  
def reseña(request):
            esp = Espacio.objects.get(id = request.POST.get('espacio'))
            ReseñaReserva.objects.create(
            text = request.POST.get('text'),
            puntaje = request.POST.get('puntaje'),
            user = request.user,
            espacio = esp
            )    
            return redirect('/')

def cambioEstadoAprobada(request):
     res = Reserva.objects.get(id = request.POST.get('id'))
     res.estado = 'aprobada'
     res.save()
     return redirect('/verperfil/')

def cambioEstadoCancelada(request):
     res = Reserva.objects.get(id = request.POST.get('id'))
     res.estado = 'cancelada'
     res.save()
     return redirect('/verperfil/')

def administrador(request):
     context = {}
     espaciosEnPausa = Espacio.objects.filter(estado = 'EnEsperaAprobacion')
     context['espaciosEnPausa'] = espaciosEnPausa

     return render(request, 'administrador.html',context) 

def cambioEspacioAprobado(request):
     esp = Espacio.objects.get(id = request.POST.get('id'))
     esp.estado = 'Publicado'
     esp.save()
     return redirect('/administrador/')

def cambioEspacioCancelado(request):
     esp = Espacio.objects.get(id = request.POST.get('id'))
     esp.estado = 'Rechazado'
     esp.save()
     return redirect('/administrador/')

def calendar_view(request):
    return render(request, 'calendario.html')

def hometest(request):
        # Obtiene el tipo de espacio del formulario enviado
    tipo = request.POST.get('tipo') 

    # Obtiene todos los objetos Espacio
    espacios2 = Espacio.objects.filter(estado = 'Publicado')

    # Obtiene el número de página actual (por defecto es 1)
    page = request.GET.get('page', 1) 

    # Filtra los espacios por el tipo especificado, si se proporciona
    if tipo:
        espacios2 = espacios2.filter(tipoEspacio = tipo)

    # Crea un objeto Paginator con 5 espacios por página
    paginator = Paginator(espacios2, 6) 

    # Obtiene la página actual de espacios
    espacios2 = paginator.page(page) 

    user = request.user

    # Prepara los datos a pasar a la plantilla 'home.html'
    data = {
        'entity':espacios2,
        'tipo': tipo,
        'paginator':paginator,
        'user': user,
        'imagen_url': '/static/img/25.jpg',  # Ajusta la ruta según la ubicación de tu imagen
    }

    # Renderiza la plantilla 'home.html' con los datos proporcionados
    return render(request, 'homatest.html', data)


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')

def base(request):
    return render(request, 'base.html')

from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event, Espacio

from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        espacio_id = self.kwargs.get('espacio_id')
        return Event.objects.filter(espacio_id=espacio_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        espacio_id = self.kwargs.get('espacio_id')
        espacio = get_object_or_404(Espacio, id=espacio_id)

        # Obtén el valor del parámetro day de la URL
        day_param = self.request.GET.get('day')
        
        # Calcula la fecha actual
        today = datetime.today()

        # Si day_param está presente y es válido, usa esa fecha, de lo contrario, usa la fecha actual
        if day_param:
            try:
                selected_date = datetime.strptime(day_param, '%Y-%m')
            except ValueError:
                selected_date = today
        else:
            selected_date = today

        # Calcula los meses anterior y siguiente
        previous_month = selected_date - timedelta(days=1)
        next_month = selected_date + timedelta(days=32)

        # Agrega la fecha actual al contexto como mes actual
        context['current_month'] = today.strftime('%Y-%m')

        # Filtra los eventos por espacio_id y el mes seleccionado
        events = Event.objects.filter(
            start_time__year=selected_date.year,
            start_time__month=selected_date.month,
            espacio_id=espacio_id
        )

        # Crea una instancia de la clase Calendar con los eventos filtrados
        cal = Calendar(selected_date.year, selected_date.month, events=events)

        # Genera el calendario como una tabla HTML
        html_cal = cal.formatmonth(withyear=True)

        # Pasa los valores al contexto
        context['calendar'] = mark_safe(html_cal)
        context['previous_month'] = previous_month.strftime('%Y-%m')
        context['next_month'] = next_month.strftime('%Y-%m')
        context['espacio'] = espacio

        return context