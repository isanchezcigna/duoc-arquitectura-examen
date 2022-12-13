from django import forms
from .models import Solicitud, Causa, Litigante, Postulacion
from django.contrib.auth.forms import UserCreationForm

CORTES = (
    ('SUPREMA', 'Suprema'),
    ('APELACIONES', 'Apelaciones'),
    ('CIVIL', 'Civil'),
    ('FAMILIA', 'Familia'),
    ('LABORAL', 'Laboral'),
    ('COBRANZA', 'Cobranza'),
    ('PENAL', 'Penal'),
)

class PostulacionForm(forms.ModelForm):
    class Meta:
        fields = ['nombre', 'rut', 'fecha_nac', 'correo', 'telefono', 'descripcion', 'requiere_material', 'requiere_lugar', 'fecha_inicio', 'fecha_fin', 'dias_impartir', 'desc_habilidades']
        model = Postulacion
        labels = {
            'nombre' : 'Nombre',
            'rut' : 'RUT',
            'fecha_nac' : 'Fecha de Nacimiento:',
            'correo' : 'Correo',
            'telefono' : 'Teléfono',
            'descripcion' : 'Descripción Taller',
            'requiere_material' : 'Requiere Material',
            'requiere_lugar' : 'Requiere Lugar',
            'fecha_inicio' : 'Desde',
            'fecha_fin' : 'Hasta',
            'dias_impartir': 'Días a Impartir',
            'desc_habilidades': 'Definición de Habilidades',
            'arch_habilidades': 'Archivo de Habilidades'
        }
        exclude = ('estado',)
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'rut': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'RUT sin puntos y con guión',
                    'id' : 'rut'
                }
            ),
            'fecha_nac': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Fecha de Nacimiento',
                    'id' : 'fecha_nac'
                }
            ),
            'correo': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'sucorreo@pagina.com',
                    'id' : 'correo'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Teléfono',
                    'id' : 'telefono'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Descripción Taller',
                    'id' : 'descripcion',
                }
            ),
            'requiere_material': forms.TextInput(
                attrs = {
                    'class' : 'form-check-input mb-3',
                    'placeholder' : 'Requiere Material',
                    'id' : 'requiere_material'
                }
            ),
            'requiere_lugar': forms.TextInput(
                attrs = {
                    'class' : 'form-check-input mb-3',
                    'placeholder' : 'Requiere Lugar',
                    'id' : 'requiere_lugar'
                }
            ),
            'fecha_inicio': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Fecha Inicio',
                    'id' : 'fecha_inicio'
                }
            ),
            'fecha_fin': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Fecha Término',
                    'id' : 'fecha_fin'
                }
            ),
            'dias_impartir': forms.TextInput(
                attrs = {
                    'class' : 'form-select mb-3',
                    'placeholder' : 'Fecha Término',
                    'id' : 'dias_impartir'
                }
            ),
            'desc_habilidades': forms.Textarea(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Definición de Habilidades',
                    'id' : 'desc_habilidades',
                }
            ),
            'arch_habilidades': forms.TextInput(
                attrs = {
                    'class' : 'mb-3',
                    'placeholder' : 'Comprobante Habilidades',
                    'id' : 'arch_habilidades'
                }
            ),
        }

class CausaForm(forms.ModelForm):
    class Meta:
        model = Causa
        fields = ['corte','tribunal','nro_causa','litigante']
        labels = {
            'corte' : 'Corte',
            'tribunal' : 'Tribunal',
            'nro_causa' : 'Número Causa',
        }

class DatosForm(forms.ModelForm):
    class Meta:
        model = Litigante
        exclude = ('user',)
        fields = ['rut', 'tipo_sujeto', 'tipo_persona','nombres','ap_paterno','ap_materno']
        labels = {
            'rut': 'Rut',
            'tipo_sujeto': 'Tipo Sujeto',
            'tipo_persona': 'Tipo Persona',
            'nombres': 'Nombres',
            'ap_paterno': 'Apellido Paterno',
            'ap_materno': 'Apellido Materno',
        }
        widgets = {
            'rut': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Rut',
                    'id' : 'rut'
                }
            ),
            'tipo_sujeto': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Tipo Sujeto',
                    'id' : 'tipo_sujeto'
                }
            ),
            'tipo_persona': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Tipo Persona',
                    'id' : 'tipo_persona'
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Nombres',
                    'id' : 'nombres'
                }
            ),
            'ap_paterno': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Apellido Paterno',
                    'id' : 'ap_paterno'
                }
            ),
            'ap_materno': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Apellido Materno',
                    'id' : 'ap_materno'
                }
            ),
        }

# class PostulacionForm(forms.ModelForm):
#     class Meta:
#         model =

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['tipo', 'asunto', 'comentario']
        labels = {
            'tipo' : 'Tipo',
            'asunto' : 'Asunto',
            'comentario' : 'Comentario',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'correo': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'correo@dominio.com',
                    'id' : 'correo'
                }
            ),
            'numero_cel': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Número Celular',
                    'id' : 'numero_cel'
                }
            ),
            'tipo' : forms.ChoiceField(choices=CORTES),
            'asunto': forms.TextInput(
                attrs = {
                    'class' : 'form-control mb-3',
                    'placeholder' : 'Especifique un Asunto',
                    'id' : 'asunto'
                }
            ),
            'comentario': forms.Textarea(
                attrs = {
                    'class' : 'form-control mb-3 comentario-height',
                    'placeholder' : 'Ingrese aquí su solicitud',
                    'id' : 'comentario',
                }
            ),

        }

class RegisterForm(UserCreationForm):
    pass