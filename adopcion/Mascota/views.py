from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm
from django.http import HttpResponseForbidden

# Create your views here.
def listado_mascota(request):
    macotas = Mascota.objects.all()  # select * from publicacion
    return render(request,'Mascota/listado_mascota.html', {'mascotas':macotas})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.save()  # Guarda la mascota en la base de datos
            return redirect('listado_mascota')  # Redirige al listado después de guardar
    else:
        form = MascotaForm()
    return render(request, 'Mascota/crear_mascota.html', {'form': form})
