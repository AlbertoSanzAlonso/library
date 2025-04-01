from django.shortcuts import render, redirect
from books.forms import EditorialModelFormCreate
from books.models import Editorial
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def editoriales_view(request):
    editoriales = Editorial.objects.all()
    context = {
        'editoriales': editoriales
    }
    return render(request, 'editoriales/editoriales.html', context)

def editorial_create_view(request):
    
    if request.method == 'POST':
        form = EditorialModelFormCreate(request.POST)
        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data['nombre'],
                direccion = form.cleaned_data['direccion'],
                ciudad = form.cleaned_data['ciudad'],
                estado = form.cleaned_data['estado'],
                pais = form.cleaned_data['pais'],
                codigo_postal = form.cleaned_data['codigo_postal'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
                sitio_web = form.cleaned_data['sitio_web'],
                fecha_fundacion = form.cleaned_data['fecha_fundacion']
            )
            
            # Redireccionar a la vista de la Editorial creada

            return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))


    else:
        form = EditorialModelFormCreate()
    context = {
        'form': form
    }    
    return render(request, 'editoriales/editorial_create.html', context)

def editorial_detail(request, id):

    editorial = Editorial.objects.get(pk=id)
    context = {
        'editorial': editorial
    }

    return render(request, 'editoriales/editorial_detail.html', context)

# Vistas basadas en clases CCBV

class EditorialListView(ListView):
    model = Editorial
    template_name = 'editoriales/EditorialList.html'
    context_object_name = 'editoriales'


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editoriales/EditorialDetail.html'
    context_object_name = 'editorial'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Esto es un titulo"
        return context
    

class EditorialCreateView(CreateView):
    model = Editorial
    template_name = 'editoriales/EditorialCreate.html'
    success_url = reverse_lazy('editorial:list')
    fields = [
        'nombre', 'direccion', 'ciudad', 'estado',
        'pais', 'codigo_postal', 'telefono', 'email',
        'sitio_web', 'fecha_fundacion'
    ]


class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = 'editoriales/EditorialUpdate.html'
    success_url = reverse_lazy('editorial:list')
    fields = [
        'nombre', 'direccion', 'ciudad', 'estado',
        'pais', 'codigo_postal', 'telefono', 'email',
        'sitio_web', 'fecha_fundacion'
    ]


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'editoriales/EditorialDelete.html'
    success_url = reverse_lazy('editorial:list')




