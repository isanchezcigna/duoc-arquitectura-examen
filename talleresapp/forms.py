from django import forms
from .models import Solicitud, Causa, Litigante
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