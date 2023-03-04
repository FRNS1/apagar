from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'cidades'

urlpatterns = [
    path('', home, name='home')
]