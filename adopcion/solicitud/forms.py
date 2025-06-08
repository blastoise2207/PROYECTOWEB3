from django import forms
from .models import Solicitud

class SolicitudAdopcionForm(forms.ModelForm):
    acepto_terminos = forms.BooleanField(
        required=True,
        label="Acepto los términos y condiciones de adopción"
    )

    class Meta:
        model = Solicitud
        fields = []