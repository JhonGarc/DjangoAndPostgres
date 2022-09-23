from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.forms import modelform_factory
from libros.models import Libro
from libros.models import LibrosBd
# aca van los metodos 

def bienvenido(request):
    numLibros = Libro.objects.count()
    libros = Libro.objects.all()
    return render(request, 'bienvenido.html',{'NumLibros' : numLibros, 'libros' : libros})

def mibiblio(request):
    myLibro = LibrosBd.objects.all()
    return render(request, 'mibiblio.html', {'libros': myLibro})




