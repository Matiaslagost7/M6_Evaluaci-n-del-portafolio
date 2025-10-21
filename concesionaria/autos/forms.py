from django import forms
from .models import Automovil

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['marca', 'modelo', 'anio', 'precio', 'stock', 'descripcion', 'imagen']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Toyota'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Corolla'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2024'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 25000'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 3', 'min': '0'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción del vehículo...'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'anio': 'Año',
            'precio': 'Precio',
            'stock': 'Stock Disponible',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
        }
        help_texts = {
            'stock': 'Cantidad de unidades disponibles. Si es 0, el vehículo se mostrará como no disponible.',
        }
