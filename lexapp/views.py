from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Causa, Recurso, Direccion, Litigante, Solicitud, Presupuesto, Pagos
from .forms import SolicitudForm, RegisterForm, DatosForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
import requests
import json

@login_required
def inicio(request):
    response = redirect('/causas')
    return response

@login_required
def causas(request):
    User = get_user_model()
    causas = Causa.objects.all()
    data = {
        'causas' : causas
    }
    #return HttpResponse(Causa.objects.all().values(),content_type="application/json")
    return render(request, 'views/causas.html', data)

def datos(request):
    data = {
        'form': DatosForm()
    }
    if request.method == 'POST':
        formulario = DatosForm(data=request.POST)
        if formulario.is_valid():
            site = formulario.save(commit=False)
            site.user = request.user
            site.save()
            messages.success(request, "¡Se han actualizado tus datos!")
            return redirect(to="causas")
    return render(request, 'views/datos.html', data)

def add_causa(request):
    response = redirect('/admin/lexapp/causa/add/')
    return response

def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    data = {
        'solicitudes' : solicitudes
    }
    return render(request, 'views/solicitudes.html', data)

def add_solicitud(request):
    response = redirect('/admin/lexapp/solicitud/add')
    return response

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

def tienda(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'views/tienda.html', data)

def nosotros(request):
    return render(request, 'views/nosotros.html')

def contacto(request):
    data = {
        'form': SolicitudForm()
    }

    if request.method == 'POST':
        formulario = SolicitudForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Se ha enviado su contacto!")

    return render(request, 'views/contacto.html', data)

def carro(request):
    return render(request, 'views/cart.html')

def api(request):
    response = request.get('#')
    array = response.json
    #print(array)

    # en la vista html: {% for data in api %} {{ data.id }} {% endfor %}
