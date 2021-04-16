from django import forms
from django.db.models import fields
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        