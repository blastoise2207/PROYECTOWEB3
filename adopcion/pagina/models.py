from django.db import models
from django.contrib.auth.models import User

class Perfil1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
