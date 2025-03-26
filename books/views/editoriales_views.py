from django.shortcuts import render
from books.forms import EditorialCreate

def editoriales_view(request):
    return render(request, 'editoriales/editoriales.html')

def editorial_create_view(request):
    
    if request.method == 'POST':
        form = EditorialCreate(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            ciudad = form.cleaned_data['ciudad']
            estado = form.cleaned_data['estado']
            pais = form.cleaned_data['pais']
            codigo_postal = form.cleaned_data['codigo_postal']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            sitio_web = form.cleaned_data['sitio_web']
            fecha_fundacion = form.cleaned_data['fecha_fundacion']
            context = {
                'nombre': nombre,
                'direccion': direccion,
                'ciudad': ciudad,
                'estado': estado,
                'pais': pais,
                'codigo_postal': codigo_postal,
                'telefono': telefono,
                'email': email,
                'sitio_web': sitio_web,
                'fecha_fundacion': fecha_fundacion
            }
    else:
        form = EditorialCreate()
    context = {
        'form': form
    }    
    return render(request, 'editoriales/editorial_create.html', context)