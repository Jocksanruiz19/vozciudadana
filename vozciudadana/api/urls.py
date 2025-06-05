from django.urls import path
from .views import (
    UserListCreate, UserUpdateDestroy,
    PostListCreate, PostUpdateDestroy,
    ComentariosListCreate, ComentariosUpdateDestroy,
    EncuestaListCreate, EncuestaUpdateDestroy,
    OpcionesListCreate, OpcionesUpdateDestroy,
    OpcionEncuestaListCreate, OpcionEncuestaUpdateDestroy,
    VotoListCreate, VotoUpdateDestroy,
    SeguidoresListCreate, SeguidoresUpdateDestroy,
    SeguidoresUsuariosListCreate, SeguidoresUsuariosUpdateDestroy
)

urlpatterns = [
    path('usuarios/', UserListCreate.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UserUpdateDestroy.as_view(), name='usuario-update-destroy'),
    
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostUpdateDestroy.as_view(), name='post-update-destroy'),
    
    path('comentarios/', ComentariosListCreate.as_view(), name='comentario-list-create'),
    path('comentarios/<int:pk>/', ComentariosUpdateDestroy.as_view(), name='comentario-update-destroy'),
    
    path('encuestas/', EncuestaListCreate.as_view(), name='encuesta-list-create'),
    path('encuestas/<int:pk>/', EncuestaUpdateDestroy.as_view(), name='encuesta-update-destroy'),
    
    path('opciones/', OpcionesListCreate.as_view(), name='opcion-list-create'),
    path('opciones/<int:pk>/', OpcionesUpdateDestroy.as_view(), name='opcion-update-destroy'),
    
    path('opciones_encuesta/', OpcionEncuestaListCreate.as_view(), name='opcion-encuesta-list-create'),
    path('opciones_encuesta/<int:pk>/', OpcionEncuestaUpdateDestroy.as_view(), name='opcion-encuesta-update-destroy'),
    
    path('votos/', VotoListCreate.as_view(), name='voto-list-create'),
    path('votos/<int:pk>/', VotoUpdateDestroy.as_view(), name='voto-update-destroy'),
    
    path('seguidores/', SeguidoresListCreate.as_view(), name='seguidor-list-create'),
    path('seguidores/<int:pk>/', SeguidoresUpdateDestroy.as_view(), name='seguidor-update-destroy'),
    
    path('seguidores_usuarios/', SeguidoresUsuariosListCreate.as_view(), name='seguidores-usuarios-list-create'),
    path('seguidores_usuarios/<int:pk>/', SeguidoresUsuariosUpdateDestroy.as_view(), name='seguidores-usuarios-update-destroy'),
]
