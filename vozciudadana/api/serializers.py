from rest_framework import serializers
from .models import Usuario, Reporte, Propuesta, Comentario, Voto, Seguidor

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class PropuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propuesta
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'

class SeguidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidor
        fields = '__all__'