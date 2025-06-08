from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm, ActualizarPerfilForm
from .models import Perfil1
from django.contrib import messages

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

def is_superuser(user):
    return user.is_superuser


def actualizar_datos(request):
    perfil, creado = Perfil1.objects.get_or_create(user=request.user, defaults={
        'ci': '',
        'telefono': '',
    })
    if request.method == 'POST':
        form = ActualizarPerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('login')
    else:
        form = ActualizarPerfilForm(instance=perfil, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })

    return render(request, 'pagina/actualizar_perfil.html', {'form': form})
def ver_perfil(request):
    perfil, created = Perfil1.objects.get_or_create(user=request.user)
    
    return render(request, 'pagina/ver_perfil.html', {
        'usuario': request.user,
        'perfil': perfil,
    })

def eliminar_cuenta(request, usuario_id):
    perfil = get_object_or_404(Perfil1, pk=usuario_id)
    user = perfil.user
    perfil.delete()
    user.delete()

    messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
    return redirect('inicio')

def confirmar_eliminar_cuenta(request):
    return render(request, 'pagina/confirmar_eliminar_cuenta.html')