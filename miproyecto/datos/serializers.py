from .models import Cliente
from .forms import ClienteForm
from rest_framework import serializers

#crear un serializador a partir de un modelo
# __all__ para incluir todos los campos del modelo

class  ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

