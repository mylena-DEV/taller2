from django.forms import forms
from .models import Cliente

#creamos un formulario a partir del modelo cliente 

class ClienteForm(forms.ModelForm):
#creamos los metadatos del formulario
    class Meta:
#establecemos el modelo y los campos que vamos a incluir
        model = Cliente
        fields = ('Cedula','Nombre','Apellido','Edad','correo','domicilio') 
        