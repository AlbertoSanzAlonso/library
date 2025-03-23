from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=140
    )
    email = forms.EmailField(
        label='Correo electrónico'
    )
    comentario = forms.CharField(
        label='Comentario',
        widget=forms.Textarea,
        max_length=1000
    )

    def clean_comentario(self):
        comentario = self.cleaned_data['comentario']
        if len(comentario) < 5:
            raise forms.ValidationError('El comentario debe tener al menos 5 caracteres')
        return comentario