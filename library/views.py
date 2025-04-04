from django.shortcuts import render
from books.models import Autor, Editorial, Libro
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _

# Vistas generales de la aplicación

def home_view(request):
    messages.info(request, _('Mensaje enviado con éxito'))
    messages.error(request, _('Se ha producido un error'))
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

