from rest_framework import viewsets

from .models import Genero, Juego, Plataforma
from .serializers import GeneroSerializer, JuegoSerializer, PlataformaSerializer

class GeneroViewset(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class PlataformaViewset(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class JuegoViewset(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
