from django.db import models
from pagina.models import Perfil1
from Mascota.models import Mascota

# Create your models here.
class Solicitud(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    usuario = models.ForeignKey(Perfil1, on_delete=models.CASCADE, related_name='solicitudes')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='solicitudes')

    def __str__(self):
        return f"Solicitud {self.id} - {self.estado}"