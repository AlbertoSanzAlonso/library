from django.shortcuts import render
from books.models import Autor, Editorial, Libro
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation
from django.http import HttpResponseRedirect
from django.views.generic import View

# Vistas generales de la aplicación

def home_view(request):
    return render(request, 'general/home.html')

def search_view(request):
    if request.GET:
        formulario = SearchForm(request.GET)
        
        busqueda = request.GET['q']
        print(formulario.data['q'])

        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)
        
        context = {
            'formulario': formulario,
            'autores': autores,
            'editoriales': editoriales,
            'libros': libros,
        }
        return render(request, "general/search.html", context)
    else:
        formulario = SearchForm()

        context = {
            'formulario': formulario,
        }

    
    return render(request, "general/search.html", context)


def contact_view(request):
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            print(f'Se ha enviado un mensaje de {nombre} con el correo {email} con el siguiente mensaje: {comentario}')
            context = {
                'formulario': formulario,
            }
            messages.info(request, _('Mensaje enviado con éxito'))
            return render(request, "general/contact.html", context)
        else:
            context = {
                'formulario': formulario,
            }
            return render(request, "general/contact.html", context)


    formulario = ContactForm()
    context = {
        'formulario': formulario,
    }
    return render(request, "general/contact.html", context)

class SetLanguageView(View):
    def post(self, request, *args, **kwargs):
        # Obtenemos el idioma seleccionado del formulario
        language = request.POST.get('language', None)

        # Si se ha seleccionado un idioma, lo activamos
        if language:
            translation.activate(language)
            request.session['django_language'] = language
        
        # Redirigimos a la página desde donde se hizo la solicitud
        next_url = request.POST.get('next', '/')
        return HttpResponseRedirect(next_url)