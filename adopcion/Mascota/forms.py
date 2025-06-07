from django import forms
from .models import Mascota, Historial_medico

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre','especie','edad','estado']

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial_medico
        fields = ['vacuna', 'tratamiento']