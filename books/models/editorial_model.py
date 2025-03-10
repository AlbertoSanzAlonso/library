from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.EmailField()
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre