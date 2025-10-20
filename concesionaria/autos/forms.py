from django import forms
from .models import Automovil

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = '__all__'
