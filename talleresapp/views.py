from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Postulacion
from .forms import RegisterForm, PostulacionForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
import requests
import json

def inicio(request):
    if request.user.is_staff: return render(request, 'views/talleres.html')
    else: return render(request, 'views/inicio.html')

@login_required
def talleres(request):
    User = get_user_model()
    #causas = Causa.objects.all()
    # data = {
    #     'causas' : causas
    # }
    #return HttpResponse(Causa.objects.all().values(),content_type="application/json")
    return render(request, 'views/talleres.html')#, data)

@login_required
def postulaciones(request):
    # User = get_user_model()
    postulaciones = Postulacion.objects.all()
    data = {
        'postulaciones' : postulaciones
    }
    #return HttpResponse(Causa.objects.all().values(),content_type="application/json")
    return render(request, 'views/postulaciones.html', data)

@login_required
def usuarios(request):
    User = get_user_model()
    users = User.objects.all()
    # causas = Causa.objects.all()
    data = {
        'users' : users
    }
    #return HttpResponse(User.objects.all().values(),content_type="application/json")
    return render(request, 'views/usuarios.html', data)

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "¡Usuario eliminado!")
    return redirect(to="usuarios", messages=messages)

def talleresdisponibles(request):
     return render(request, 'views/talleres-disponibles.html')


def registro(request):
    data = {
        'form': RegisterForm()
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(request, username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "¡Registro correcto! Inicie sesión")
            return redirect(to="login")
    return render(request, 'registration/registro.html', data)

def cuenta(request):
    return render(request, 'views/cuenta.html')

# def nosotros(request):
#     return render(request, 'views/nosotros.html')

def postulacion(request):
    data = {
        'form': PostulacionForm()
    }

    if request.method == 'POST':
        formulario = PostulacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Se ha enviado su solicitud!")

    return render(request, 'views/postulacion.html', data)
    #return render(request, 'views/postulacion.html')

# def carro(request):
#     return render(request, 'views/cart.html')

# def api(request):
#     response = request.get('#')
#     array = response.json
    #print(array)

    # en la vista html: {% for data in api %} {{ data.id }} {% endfor %}
