from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'propuestas', PropuestaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'votos', VotoViewSet)
router.register(r'seguidores', SeguidorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]