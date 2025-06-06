from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from .models import Perfil1

def inicio(request):
    return render(request, 'pagina/inicio.html')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            ci = form.cleaned_data['ci']
            telefono = form.cleaned_data['telefono']

            user = User.objects.create_user(
                username=email,
                first_name=nombre,
                last_name=apellido,
                email=email,
                password=password
            )

            Perfil1.objects.create(user=user, ci=ci, telefono=telefono)

            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'pagina/registro.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
                else:
                    error = "Correo o contraseña incorrectos"
            except User.DoesNotExist:
                error = "Correo o contraseña incorrectos"
    else:
        form = LoginForm()

    return render(request, 'pagina/login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('inicio')
