from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label=_('Nombre'),
        max_length=140
    )
    email = forms.EmailField(
        label=_('Correo electrónico')
    )
    comentario = forms.CharField(
        label=_('Comentario'),
        widget=forms.Textarea,
        max_length=1000
    )

    def clean_comentario(self):
        comentario = self.cleaned_data['comentario']
        if len(comentario) < 5:
            raise forms.ValidationError(_('El comentario debe tener al menos 5 caracteres'))
        return comentario