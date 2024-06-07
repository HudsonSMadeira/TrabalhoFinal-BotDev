from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from .models import *

def paginaInicial(request):
    return render(request,'paginaInicial.html')

def reactpagina1(request):
    return render(request,'reactpagina1.html')

def reactpagina2(request):
    return render(request,'reactpagina2.html')

def javascriptpagina1(request):
    return render(request,'javascriptpagina1.html')

def javascriptpagina2(request):
    return render(request,'javascriptpagina2.html')

def htmlpagina1(request):
    return render(request,'htmlpagina1.html')

def htmlpagina2(request):
    return render(request,'htmlpagina2.html')

def frameworkpagina1(request):
    return render(request,'frameworkpagina1.html')

def frameworkpagina2(request):
    return render(request,'frameworkpagina2.html')





