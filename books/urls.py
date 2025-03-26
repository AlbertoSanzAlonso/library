from django.urls import path
from .views import autores_view, editoriales_view, libros_view, autor_detail, editorial_create_view

app_name = 'books'

urlpatterns = [
    path('autores/', autores_view, name="autor_list"),   
    path('autores/<int:id>/', autor_detail, name="autor_detail"),   
    path('libros/', libros_view, name="libros_list"),   
    path('editoriales/', editoriales_view, name="editoriales_list"),  
    path('editoriales/create/', editorial_create_view, name="editorial_create"),
] 
