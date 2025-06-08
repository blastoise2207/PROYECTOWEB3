from django.urls import path
from . import views
urlpatterns = [
    path('solicitar/<int:mascota_id>/', views.solicitar_adopcion, name='solicitar_adopcion'),
    path('confirmacion/<int:solicitud_id>/', views.confirmacion_solicitud, name='confirmacion_solicitud'),
    path('listado_soicitud/', views.listado_solicitud, name='listado_solicitud'),
    path('listado_soicitud2/', views.listado_solicitud2, name='listado_solicitud2'),
    path('solicitud/<int:solicitud_id>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
]