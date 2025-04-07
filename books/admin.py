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

def set_out_stock(modeladmin, request, queryset):
    queryset.update(is_out_stock=True)
    modeladmin.message_user(request, "Libros marcados como fuera de stock")
    
set_out_stock.short_description = "Marcar libros como fuera de stock"

def export_books_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=libros.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Titulo', 'ISBN', 'Editorial'])
    for libro in queryset:
        writer.writerow([libro.id, libro.titulo, libro.isbn, libro.editorial])
    return response
export_books_to_csv.short_description = "Exportar libros a CSV"


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_filter = ['editorial', 'idioma']
    list_display = ('titulo', 'isbn', 'editorial', 'idioma', 'is_out_stock')
    filter_horizontal = ('autores',)
    actions = [set_out_stock, export_books_to_csv,]
   

