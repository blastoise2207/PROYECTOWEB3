from django.db import models
from django.contrib.auth.models import User

class Perfil1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Mascota(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Historial_medico(models.Model):
    id = models.IntegerField(primary_key=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    vacuna = models.CharField(max_length=100)
    tratamiento = models.TextField(max_length=100)