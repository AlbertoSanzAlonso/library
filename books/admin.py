from django.contrib import admin

# Register your models here.

from django.contrib import admin
from books.models import Autor, Editorial, Libro


class BookInline(admin.TabularInline):
    model = Libro

class BookInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',
                    'fecha_nacimiento',
                    'nacionalidad'
                    )
   
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'fecha_fundacion')
    list_filter = ('fecha_fundacion', 'direccion')
    search_fields = ('direccion',)
    ordering = ('fecha_fundacion',)
    inlines = [
        BookInline,
    ]



@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_filter = ['editorial', 'idioma']
    list_display = ('titulo', 'isbn', 'editorial', 'idioma')
    filter_horizontal = ('autores',)
   
