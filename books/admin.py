from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from books.models import Autor, Editorial, Libro
from simple_history.models import HistoricalRecords


# Register your models here.



class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'email',)
        import_order = ('id', 'nombre',)
        export_order = ('id', 'nombre', 'apellido',)


class BookInline(admin.TabularInline):
    model = Libro

class BookInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AutorResource
    list_display = ('nombre',
                    'fecha_nacimiento',
                    'nacionalidad'
                    )
    history = HistoricalRecords()
   
    

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
   

