from django.shortcuts import render
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', paginaInicial, name='paginaInicial'),
    path('reactpagina1', reactpagina1, name='reactpagina1'),
    path('reactpagina2', reactpagina2, name='reactpagina2'),
    path('javascriptpagina1', javascriptpagina1, name='javascriptpagina1'),
    path('javascriptpagina2', javascriptpagina2, name='javascriptpagina2'),
    path('htmlpagina1', htmlpagina1, name='htmlpagina1'),
    path('htmlpagina2', htmlpagina2, name='htmlpagina2'),
    path('frameworkpagina1', frameworkpagina1, name='frameworkpagina1'),
    path('frameworkpagina2', frameworkpagina2, name='frameworkpagina2'),
]
