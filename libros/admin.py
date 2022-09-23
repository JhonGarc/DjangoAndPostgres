from django.contrib import admin

# Register your models here.

from libros.models import Libro

from libros.models import LibrosBd

admin.site.register(Libro)
admin.site.register(LibrosBd)