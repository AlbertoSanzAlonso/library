from django.urls import path
from books.views import *

app_name = 'libro'


urlpatterns = [
    path('libros/', LibrosListView.as_view(), name="list"),
    path('libros/create', CreateBookView.as_view(), name="create"), 
    path('libros/editar/<int:pk>/', LibrosUpdateView.as_view(), name="editar"),
    path('libros/delete/<int:pk>/', LibrosDeleteView.as_view(), name='delete'),
]

