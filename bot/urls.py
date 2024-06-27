from django.shortcuts import render
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', paginaInicial, name='paginaInicial'),
    path('reactpagina1', reactpagina1, name='reactpagina1'),
    path('reactpagina2', reactpagina2, name='reactpagina2'),
    path('reactpagina3', reactpagina3, name='reactpagina3'),
    path('reactpagina4', reactpagina4, name='reactpagina4'),
    path('reactpagina5', reactpagina5, name='reactpagina5'),
    path('reactpagina6', reactpagina6, name='reactpagina6'),
    path('reactpagina7', reactpagina7, name='reactpagina7'),

    path('javascriptpagina1', javascriptpagina1, name='javascriptpagina1'),
    path('javascriptpagina2', javascriptpagina2, name='javascriptpagina2'),
    path('javascriptpagina3', javascriptpagina3, name='javascriptpagina3'),
    path('javascriptpagina4', javascriptpagina4, name='javascriptpagina4'),
    path('javascriptpagina5', javascriptpagina5, name='javascriptpagina5'),
    path('javascriptpagina6', javascriptpagina6, name='javascriptpagina6'),
    path('javascriptpagina7', javascriptpagina7, name='javascriptpagina7'),


    path('htmlpagina1', htmlpagina1, name='htmlpagina1'),
    path('htmlpagina2', htmlpagina2, name='htmlpagina2'),
    path('frameworkpagina1', frameworkpagina1, name='frameworkpagina1'),
    path('frameworkpagina2', frameworkpagina2, name='frameworkpagina2'),
]
