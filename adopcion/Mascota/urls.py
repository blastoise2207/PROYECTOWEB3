from django.urls import path
from . import views

urlpatterns = [
    path('listado_mascotas/', views.listado_mascota, name='listado_mascota'),
    path('agregar_mascota/', views.crear_mascota, name='agregar_mascota'),
]