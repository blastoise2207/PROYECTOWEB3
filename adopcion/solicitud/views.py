from django.shortcuts import render, redirect, get_object_or_404
from Mascota.models import Mascota
from .models import Solicitud
from pagina.models import Perfil1
from .forms import SolicitudAdopcionForm
from django.http import HttpResponseForbidden
from django.contrib import messages

def solicitar_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    perfil = request.user.perfil1
    if mascota.estado == 'adoptado':
        messages.warning(request, "Esta mascota ya fue adoptada.")
        return redirect('listado_mascota')
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            existe = Solicitud.objects.filter(usuario=perfil, mascota=mascota).exists()
            if existe:
                messages.warning(request, "Ya has solicitado adoptar esta mascota.")
                return redirect('listado_mascota')

            solicitud = form.save(commit=False)
            solicitud.usuario = perfil
            solicitud.mascota = mascota
            solicitud.save()
            return redirect('confirmacion_solicitud', solicitud_id=solicitud.id)
    else:
        form = SolicitudAdopcionForm()

    return render(request, 'solicitud/form_solicitud.html', {'form': form , 'mascota': mascota})
  
def confirmacion_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    return render(request, 'solicitud/confirmacion_solicitud.html', {
        'solicitud': solicitud
    })

def listado_solicitud(request):
    perfil = Perfil1.objects.get(user=request.user)
    solicitudes = Solicitud.objects.filter(usuario=perfil)
    return render(request, 'solicitud/listado_solicitud.html', {'solicitud': solicitudes})

def listado_solicitud2(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'solicitud/listado_solicitud.html', {'solicitud': solicitudes})

def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
    perfil = Perfil1.objects.get(user=request.user)

    if solicitud.usuario != perfil and not request.user.is_superuser:
        return HttpResponseForbidden("No tenés permiso para eliminar esta solicitud.")
    solicitud.delete()
    return redirect('listado_solicitud')

def eliminar_solicitud2(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, pk=solicitud_id)
    perfil = Perfil1.objects.get(user=request.user)

    if solicitud.usuario != perfil and not request.user.is_superuser:
        return HttpResponseForbidden("No tenés permiso para eliminar esta solicitud.")
    solicitud.delete()
    return redirect('listado_solicitud2')