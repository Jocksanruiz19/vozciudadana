from rest_framework import viewsets
from .models import *
from .serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class PropuestaViewSet(viewsets.ModelViewSet):
    queryset = Propuesta.objects.all()
    serializer_class = PropuestaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class SeguidorViewSet(viewsets.ModelViewSet):
    queryset = Seguidor.objects.all()
    serializer_class = SeguidorSerializer