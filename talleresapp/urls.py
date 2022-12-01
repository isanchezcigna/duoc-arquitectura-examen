from django.contrib import admin
from django.urls import path, include
from .views import inicio, talleres, cuenta, tienda, nosotros, solicitudes, api, registro, add_causa, add_solicitud, datos, postulacion, admin_user

urlpatterns = [
    path('', inicio, name="inicio"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', registro, name="registro"),
    path('talleres', talleres, name="talleres"),
    path('caja', nosotros, name="nosotros"),      
    path('solicitudes', solicitudes, name="solicitudes"),
    path('usuarios', tienda, name="tienda"),
    path('add_causa', add_causa, name="add_causa"),
    path('add_solicitud', add_solicitud, name="add_solicitud"),
    path('datos', datos, name="datos"),
    path('postulacion', postulacion, name="postulacion"),
    path('admin_user', admin_user, name="admin_user"),

]

'''Causas | Usuarios | Caja - Informe Ingresos | Presupuesto | Solicitudes'''

''' usuario comun / tecnico juridico / abogado admin '''