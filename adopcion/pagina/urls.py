from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/actualizar/', views.actualizar_datos, name='actualizar_perfil_superusuario'),
    path('perfil/ver/', views.ver_perfil, name='ver_perfil'),
    path('eliminar_cuenta/<int:usuario_id>/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('confirmar_eliminar_cuenta/', views.confirmar_eliminar_cuenta, name='confirmar_eliminar_cuenta'),
]
