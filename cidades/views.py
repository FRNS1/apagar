from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .utils import *

# Create your views here.


def home(request):
    lista_cidades = []
    if request.method == 'POST':
        estado = request.POST.get('estado')
        print(estado)
        lista_cidades = ferramentas.ConsomeApi(estado)
    context = {'lista_cidades': lista_cidades}
    return render(request, 'index.html', context)
