from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        label='Introduce tu búsqueda',
        max_length=100
    )