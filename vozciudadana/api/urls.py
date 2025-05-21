from rest_framework import routers
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'propuestas', PropuestaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'votos', VotoViewSet)
router.register(r'seguidores', SeguidorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]