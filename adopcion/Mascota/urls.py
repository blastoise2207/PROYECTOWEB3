from django.urls import path
from . import views

urlpatterns = [
    path('listado_mascotas/', views.listado_mascota, name='listado_mascota'),
    path('agregar_mascota/', views.crear_mascota, name='agregar_mascota'),
    path('<int:mascota_id>',views.Historial_Mascota,name='mascota'),
    path('mascota/<int:mascota_id>/agregar_historial/', views.agregar_historial, name='agregar_historial'),
    path('historial/<int:historial_id>/eliminar/', views.eliminar_historial, name='eliminar_historial'),
    path('mascota/<int:mascota_id>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascota/editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('historial/editar/<int:pk>/', views.editar_historial, name='editar_historial'),
]