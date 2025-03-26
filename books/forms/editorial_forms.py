from django import forms

class EditorialCreate(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=200)
    direccion = forms.CharField(label='Dirección', max_length=300, required=False)
    ciudad = forms.CharField(label='Ciudad', max_length=100, required=False)
    estado = forms.CharField(label='Estado', max_length=100, required=False)
    pais = forms.CharField(label='País', max_length=100, required=False)
    codigo_postal = forms.CharField(label='Código Postal', max_length=20, required=False)
    telefono = forms.CharField(label='Teléfono', max_length=20, required=False)
    email = forms.EmailField(label='Email')
    sitio_web = forms.EmailField(label='Sitio Web', required=False)
    fecha_fundacion = forms.DateField(label='Fecha de Fundación')