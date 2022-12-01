from django.contrib import admin
from .models import Causa, Recurso, Direccion, Litigante, Solicitud, Presupuesto, Pagos
# Register your models here.

admin.site.register(Causa)
admin.site.register(Recurso)
admin.site.register(Direccion)
admin.site.register(Litigante)
admin.site.register(Solicitud)
admin.site.register(Presupuesto)
admin.site.register(Pagos)