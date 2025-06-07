from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)   #models.TextField()
    edad = models.CharField(max_length=50)      #models.TextField()
    estado = models.TextField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return ({self.nombre},{self.especie},{self.edad},{self.estado},{self.fecha_ingreso})