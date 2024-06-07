from django.shortcuts import render
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', paginaInicial, name='paginaInicial'),
    path('pagina1', pagina1, name='pagina1'),
    path('pagina2', pagina2, name='pagina2'),
    path('pagina3', pagina3, name='pagina3'),
    path('pagina4', pagina4, name='pagina4'),
  
]

