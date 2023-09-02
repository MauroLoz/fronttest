
# Importar formularios 
from django import forms

# Se importan modelos Espacio y Reserva desde el archivo models.py.
from .models import Espacio, Reserva, ReseñaReserva

# Definir clases de formularios, para ser representados y validados

# Formulario del modelo Espacio

# Se traen todos los atributos del modelo espacio al form
class espacioForm(forms.ModelForm):
   class Meta:
      model = Espacio 

      # Campos excluidos del formulario
      exclude = ('user',)

      # Todos los campos del modelo se incluyen en el formulario
      fields = "__all__"

      # Configuración de widgets para los campos del formulario
      widgets = {
         'titulo': forms.TextInput(attrs={'class': 'form-control', }),
         'descripcion': forms.Textarea(attrs={'class': 'form-control', 'style':'height: 100px'}),
         'image1': forms.FileInput(attrs={'class': 'form-control form-control-sm my-3', 'type':'file'}),
         'image2': forms.FileInput(attrs={'class': 'form-control form-control-sm my-3', 'type':'file'}),
         'image3': forms.FileInput(attrs={'class': 'form-control form-control-sm my-3', 'type':'file'}),
         'tipoEspacio': forms.Select(attrs={'class': 'custom-select'}),
         'superficie' : forms.NumberInput(attrs={'class': 'form-control'}),
         'baño': forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox01'}),
         'estacionamiento' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox02'}),
         'calefaccion' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox03'}),
         'aire' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox04'}),
         'techo' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox05'}),
         'lineaTelefonica' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox06'}),
         'agua' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox07'}),
         'wifi' : forms.CheckboxInput(attrs={'type':'checkbox', 'class': 'custom-control-input', 'id':'espacioCheckbox08'}),
         'direccion': forms.TextInput(attrs={'class': 'form-control', }),
      }


# Formulario del modelo Reserva
class reservaForm(forms.ModelForm):
   class Meta:
      model = Reserva

      # Campos excluidos del formulario
      exclude = ('user', 'post')
       

      widgets = {
         'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre..'}),
         'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellido..'}),
         'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'DNI..'}),
         'nroCelular': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nro Celular'}),
         'fecha': forms.DateInput(attrs={'class': 'form-control',}),
         'hora': forms.TimeInput(attrs={'class': 'form-control', }),
         'tipoPago': forms.Select(attrs={'class': 'custom-select'}),
      }


class reseñaForm(forms.ModelForm):
   class Meta:
      model = ReseñaReserva

      exclude = ('user', 'espacio')
