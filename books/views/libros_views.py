from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DeleteView
from django.views.generic.list import ListView
from books.models import Libro
from django.urls import reverse_lazy


class LibrosListView(ListView):
    model = Libro
    template_name = "libros/LibrosList.html"
    context_object_name = "libros"


class CreateBookView(CreateView):
    model = Libro
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
    ]
    template_name = 'libros/LibrosCreate.html'
    success_url = reverse_lazy("libro:create")

    
class LibrosUpdateView(UpdateView):
    model = Libro
    template_name = 'libros/LibrosUpdate.html'
    fields = [
        "titulo",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
    ]
    success_url = reverse_lazy('libro:list')

class LibrosDeleteView(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro:list')
    template_name = 'libros/LibrosDelete.html'
