from django.urls import path
from books.views import autor_detail, autores_view

app_name = 'autor'

urlpatterns = [
    path('autores/', autores_view, name="list"),  
    path('autores/<int:id>/', autor_detail, name="detail"),
]
