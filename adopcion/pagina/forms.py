from django import forms
from django.contrib.auth.models import User
from .models import Perfil1

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    ci = forms.CharField(label="CI")
    telefono = forms.CharField(label="Teléfono")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Las contraseñas no coinciden.")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class ActualizarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', max_length=150)
    last_name = forms.CharField(label='Apellido', max_length=150)
    email = forms.EmailField(label='Correo')
    nueva_contraseña = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = Perfil1
        fields = ['ci', 'telefono']

    def save(self, user, commit=True):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        nueva_contraseña = self.cleaned_data.get('nueva_contraseña')
        if nueva_contraseña:
            user.set_password(nueva_contraseña)

        if commit:
            user.save()
            perfil = super().save(commit=False)
            perfil.user = user
            perfil.save()
        return user