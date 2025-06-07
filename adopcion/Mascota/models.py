from django.db import models

class Mascota(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)      

    def __str__(self):
        return ({self.nombre},{self.especie},{self.edad},{self.estado},{self.fecha_ingreso})

class Historial_medico(models.Model):
    id = models.IntegerField(primary_key=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    vacuna = models.CharField(max_length=100)
    tratamiento = models.TextField(max_length=100)
