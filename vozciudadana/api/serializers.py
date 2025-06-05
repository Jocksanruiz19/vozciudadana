from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class SeguidoresSerializer(serializers.ModelSerializer):
    class Meta:
     model = SeguidoresUsuarios
     fields = '__all__'



class SeguidoresUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguidoresUsuarios
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'

class OpcionEncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionEncuesta
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'