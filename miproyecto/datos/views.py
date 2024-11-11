from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
#creamos una vista a partir de un serializador
class ClienteViewSet(viewsets.ModelViewSet):
#hacemos una query para traer todos los objetos del modelo cliente
    queryset = Cliente.objects.all()
#llamamos al serializador q vamos a incluir en la vista
    serializer_class = ClienteSerializer
    