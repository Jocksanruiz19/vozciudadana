from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)

class Reporte(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('resuelto', 'Resuelto'),
    ]
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Propuesta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)

class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE)

class Seguidor(models.Model):
    seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguido')
    seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidor')