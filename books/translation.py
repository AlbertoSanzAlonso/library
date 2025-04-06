from modeltranslation.translator import translator, TranslationOptions
from .models import Libro
from books.views.libros_views import CreateBookView

class LibroTranslationOptions(TranslationOptions):
    fields = ('titulo', 'idioma', 'descripcion', 'genero')
   
translator.register(Libro, LibroTranslationOptions)

