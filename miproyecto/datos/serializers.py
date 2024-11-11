from .models import Cliente
from rest_framework import serializers

#crear un serializador a partir de un modelo
#el serializador convierte los registros en formato json
# __all__ para incluir todos los campos del modelo

class  ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

