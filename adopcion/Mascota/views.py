from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Historial_medico
from .forms import MascotaForm, HistorialForm

# Create your views here.
def listado_mascota(request):
    macotas = Mascota.objects.all()
    return render(request,'Mascota/listado_mascota.html', {'mascotas':macotas})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.save()
            return redirect('listado_mascota')
    else:
        form = MascotaForm()
    return render(request, 'Mascota/crear_mascota.html', {'form': form})

def Historial_Mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    historiales = Historial_medico.objects.filter(mascota_id=mascota).order_by('-fecha')

    return render(request, 'Mascota/historial.html', {
        'mascota': mascota,
        'historiales': historiales
    })

def agregar_historial(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            historial = form.save(commit=False)
            historial.mascota_id = mascota
            historial.save()
            return redirect('mascota', mascota_id=mascota.id)
    else:
        form = HistorialForm()

    return render(request, 'Mascota/agregar_historial.html', {'form': form, 'mascota': mascota})

def eliminar_historial(request, historial_id):
    historial = get_object_or_404(Historial_medico, pk=historial_id)
    mascota_id = historial.mascota_id.id
    historial.delete()
    return redirect('mascota', mascota_id=mascota_id)

# Eliminar mascota
def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    mascota.delete()
    return redirect('listado_mascota')

def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listado_mascota')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'Mascota/editar_mascota.html', {'form': form})

def editar_historial(request, pk):
    historial = get_object_or_404(Historial_medico, pk=pk)
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('mascota', mascota_id=historial.mascota_id.id)
    else:
        form = HistorialForm(instance=historial)
    return render(request, 'Mascota/editar_historial.html', {'form': form})