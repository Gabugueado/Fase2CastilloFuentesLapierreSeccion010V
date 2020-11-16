from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'nombre',
            'descripcion',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
        }