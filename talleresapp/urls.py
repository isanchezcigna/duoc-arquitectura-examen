from django.contrib import admin
from django.urls import path, include
from .views import inicio, talleres, cuenta,  registro, postulacion, talleresdisponibles, postulaciones, usuarios, eliminar_usuario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', registro, name="registro"),
    path('talleres', talleres, name="talleres"),
    # path('caja', nosotros, name="nosotros"),      
    # path('solicitudes', solicitudes, name="solicitudes"),
    path('usuarios', usuarios, name="usuarios"),
    # path('add_taller', add_taller, name="add_taller"),
    # path('add_user', add_user, name="add_user"),
    # path('datos', datos, name="datos"),
    path('postulacion', postulacion, name="postulacion"),
    path('postulaciones', postulaciones, name="postulaciones"),
    path('usuarios', usuarios, name="usuarios"),
    path('eliminar-usuario/<int:id>/', eliminar_usuario, name="eliminar_usuario"),
    # path('admin_user', admin_user, name="admin_user"),
    path('talleresdisponibles', talleresdisponibles, name="talleresdisponibles"),

]

'''Causas | Usuarios | Caja - Informe Ingresos | Presupuesto | Solicitudes'''

''' usuario comun / tecnico juridico / abogado admin '''