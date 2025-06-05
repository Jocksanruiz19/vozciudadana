from django.contrib.auth.models import User
from rest_framework.generics import *
from .models import (
    User, Post, Comentarios, Encuesta, Opciones, OpcionEncuesta,
    Voto, Seguidores, SeguidoresUsuarios
)
from .serializers import (
    UserSerializer, PostSerializer, ComentariosSerializer, EncuestaSerializer,
    OpcionesSerializer, OpcionEncuestaSerializer, VotoSerializer,
    SeguidoresSerializer, SeguidoresUsuariosSerializer
)


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ComentariosListCreate(ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

class ComentariosUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer


class EncuestaListCreate(ListCreateAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

class EncuestaUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


class OpcionesListCreate(ListCreateAPIView):
    queryset = Opciones.objects.all()
    serializer_class = OpcionesSerializer

class OpcionesUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Opciones.objects.all()
    serializer_class = OpcionesSerializer


class OpcionEncuestaListCreate(ListCreateAPIView):
    queryset = OpcionEncuesta.objects.all()
    serializer_class = OpcionEncuestaSerializer

class OpcionEncuestaUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = OpcionEncuesta.objects.all()
    serializer_class = OpcionEncuestaSerializer


class VotoListCreate(ListCreateAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class VotoUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer


class SeguidoresListCreate(ListCreateAPIView):
    queryset = Seguidores.objects.all()
    serializer_class = SeguidoresSerializer

class SeguidoresUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Seguidores.objects.all()
    serializer_class = SeguidoresSerializer


class SeguidoresUsuariosListCreate(ListCreateAPIView):
    queryset = SeguidoresUsuarios.objects.all()
    serializer_class = SeguidoresUsuariosSerializer

class SeguidoresUsuariosUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = SeguidoresUsuarios.objects.all()
    serializer_class = SeguidoresUsuariosSerializer