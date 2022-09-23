from django.db import models

# Create your models here.

class Libro(models.Model):
    Titulo = models.CharField(max_length = 255)
    Autor = models.CharField(max_length = 255)
    Genero = models.CharField(max_length = 255)
    Descripcion = models.CharField(max_length = 255)
    FechaCompra = models.DateField(null=True, blank=True)
    estadoLectura = models.CharField(max_length = 255, null = True)
    numeroPaginas = models.IntegerField(null=True, blank=True)
    numeroLeidas = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return f'Libro {self.id} : {self.Titulo} {self.Autor} {self.Genero} {self.Descripcion} {self.FechaCompra} {self.estadoLectura} {self.numeroPaginas} {self.numeroLeidas}' 


class LibrosBd(models.Model):
    Titulo = models.CharField(max_length=255)
    Autor = models.CharField(max_length=255)
    Genero = models.CharField(max_length=255)
    Descripcion = models.CharField(max_length=255)
    FechaCompra = models.DateField(null=True, blank=True)
    estadoLectura = models.CharField(max_length=255, null=True)
    numeroPaginas = models.IntegerField(null=True, blank=True)
    numeroLeidas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Libro {self.id} : {self.Titulo} {self.Autor} {self.Genero} {self.Descripcion} {self.FechaCompra} {self.estadoLectura} {self.numeroPaginas} {self.numeroLeidas}'
