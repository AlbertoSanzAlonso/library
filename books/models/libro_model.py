from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial

class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    LANG_CHOICES = {
                    "ES": 'Español',
                    "EN": 'Ingles'
                    }

    idioma = models.CharField(max_length=2, choices=LANG_CHOICES, default='ES', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True, blank=True)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_out_stock = models.BooleanField('Está fuera de stock', default=False)

    def __str__(self):
        return self.titulo