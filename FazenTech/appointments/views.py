from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Vacas, RegistroLeite, Filhote, Administrador, Funcionarios

def lista_vacas(request):
    vacas = Vacas.objects.all()
    return render(request, 'vacas.html', {'vacas': vacas})

def lista_registro_leite(request):
    registros = RegistroLeite.objects.all()
    return render(request, 'registro_leite.html', {'registros': registros})

def lista_filhotes(request):
    filhotes = Filhote.objects.all()
    return render(request, 'filhotes.html', {'filhotes': filhotes})

def lista_administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'administradores.html', {'administradores': administradores})

def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios})
