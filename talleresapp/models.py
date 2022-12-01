from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Litigante(models.Model):
    rut = models.CharField(max_length=13)
    tipo_sujeto = models.CharField(max_length=200)
    tipo_persona = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    ap_paterno = models.CharField(max_length=200)
    ap_materno = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __int__(self):
        return self.user.id

    class Meta:
        db_table = 'litigante'
        verbose_name = 'Litigante'
        verbose_name_plural = 'Litigantes'
        ordering = ['id']  

class Causa(models.Model):
    class Corte(models.TextChoices):
        Suprema = 'Suprema'
        Apelaciones = 'Apelaciones'
        Civil = 'Civil'
        Familia = 'Familia'
        Laboral = 'Laboral'
        Cobranza = 'Cobranza'
        Penal = 'Penal'

    corte = models.CharField(choices=Corte.choices, max_length=200)
    tribunal = models.CharField(max_length=200)
    nro_causa = models.IntegerField(null=False)
    fecha_ingreso = models.DateTimeField(editable=False, auto_now_add=True)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)

    def __str__(self):
        return self.corte

    class Meta:
        db_table = 'causa'
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'
        ordering = ['id']

class Recurso(models.Model):
    libro = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    causa = models.ForeignKey(Causa, on_delete=models.PROTECT,)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'recurso'
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
        ordering = ['id']    

class Direccion(models.Model):
    region = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.observacion

    class Meta:
        db_table = 'direccion'
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
        ordering = ['id']  

class Solicitud(models.Model):
    class Tipo(models.TextChoices):
        SUPREMA = 'Suprema'
        APELACIONES = 'Apelaciones'
        CIVIL = 'Civil'
        FAMILIA = 'Familia'
        LABORAL = 'Laboral'
        COBRANZA = 'Cobranza'
        PENAL = 'Penal'
    tipo = models.IntegerField(choices=Tipo.choices)
    asunto = models.CharField(max_length=200)
    comentario = models.CharField(max_length=200)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)
    fecha = models.DateTimeField(editable=False, auto_now_add=True)
    
    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'solicitud'
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['id']

class Presupuesto(models.Model):
    valor = models.IntegerField(null=True)
    causa = models.ForeignKey('Causa', on_delete=models.PROTECT,)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)

    class Meta:
        db_table = 'presupuesto'
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'
        ordering = ['id']

class Pagos(models.Model):
    class Estado(models.IntegerChoices):
        GENERADO = 1
        PAGADO = 2
        RECHAZADO = 3
        IMPAGO = 4
        MORA = 5
        COBRANZA = 6
    causa = models.ForeignKey('Causa', on_delete=models.CASCADE,)
    litigante = models.ForeignKey(Litigante, on_delete=models.PROTECT)
    pago = models.IntegerField(null=True)
    estado = models.IntegerField(choices=Estado.choices)
    fecha = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.pago

    class Meta:
        db_table = 'pago'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['id']        