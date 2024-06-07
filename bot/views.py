from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from .models import *

def paginaInicial(request):
    return render(request,'paginaInicial.html')

def pagina1(request):
    return render(request,'pagina1.html')

def pagina2(request):
    return render(request,'pagina2.html')

def pagina3(request):
    return render(request,'pagina3.html')

def pagina4(request):
    return render(request,'pagina4.html')

