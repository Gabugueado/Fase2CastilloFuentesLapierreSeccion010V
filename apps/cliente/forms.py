from django import forms
from apps.cliente.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

# class ClienteForm(forms.ModelForm):
#     class Meta:
#         model = Cliente
#         fields = [
#             'nombre',
#             'apellido',
#             'edad',
#             'email',
#             'direccion',
#         ]
#         labels = {
#             'nombre': 'Nombres',
#             'apellido': 'Apellidos',
#             'edad': 'Edad',
#             'email': 'Correo_Electronico',
#             'direccion': 'Direccion',
#         }
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class':'form-control'}),
#             'apellido': forms.TextInput(attrs={'class':'form-control'}),
#             'edad': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.TextInput(attrs={'class':'form-control'}),
#             'direccion': forms.TextInput(attrs={'class':'form-control'}),
#         }