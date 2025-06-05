from django.db import models
from django.contrib.auth.models import User

""""
class Usuario(models.Model): 
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre
"""
class Seguidores(models.Model):
    nombre_seguidores = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_seguidores

class SeguidoresUsuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    seguidores = models.ForeignKey(Seguidores, on_delete=models.CASCADE)

class Post(models.Model):
    contenido = models.TextField()
    fecha_post = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentarios(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Opciones(models.Model):
    nombre = models.CharField(max_length=100)

class OpcionEncuesta(models.Model):
    opcion = models.ForeignKey(Opciones, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opciones, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)