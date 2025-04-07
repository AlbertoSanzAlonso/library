from django import forms
from books.models import Editorial
from django.utils.translation import gettext_lazy as _

# class EditorialCreate(forms.Form):
#     nombre = forms.CharField(label=_('Nombre'), max_length=200)
#     direccion = forms.CharField(label=_('Dirección'), max_length=300, required=False)
#     ciudad = forms.CharField(label=_('Ciudad'), max_length=100, required=False)
#     estado = forms.CharField(label=_('Estado'), max_length=100, required=False)
#     pais = forms.CharField(label=_('País'), max_length=100, required=False)
#     codigo_postal = forms.CharField(label=_('Código Postal'), max_length=20, required=False)
#     telefono = forms.CharField(
#         label=_('Teléfono'), 
#         max_length=11, 
#         required=False, 
#         widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '+34 123 456 789'})
#     )
#     email = forms.EmailField(label=_('Email'))
#     sitio_web = forms.URLField(
#         label=_('Sitio Web'), 
#         required=False, 
#         widget=forms.TextInput(attrs={'placeholder': 'https://www.ejemplo.com', 'class': 'form-control'})
#     )
#     fecha_fundacion = forms.DateField(label=_('Fecha de Fundación'), widget=forms.SelectDateWidget)

#     def clean_nombre(self):
#         nombre = self.cleaned_data['nombre']
#         if len(nombre) < 5:
#             raise forms.ValidationError('El nombre debe tener al menos 5 caracteres')
#         return nombre 
    
class EditorialModelFormCreate(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = (
            'nombre', 
            'direccion', 
            'email', 
            'fecha_fundacion',
            'nivel'
        )
        labels = {
            'nombre': _('Nombre'),
            'direccion': _('Dirección'),
            'email': _('Email'),
            'fecha_fundacion': _('Fecha de Fundación'),
            'nivel': _('Nivel'),
        }
