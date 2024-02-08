from django.urls import path
from .views import lista_vacas, lista_registro_leite, lista_filhotes, lista_administradores, lista_funcionarios

urlpatterns = [
    path('vacas/', lista_vacas, name='lista_vacas'),
    path('registro_leite/', lista_registro_leite, name='lista_registro_leite'),
    path('filhotes/', lista_filhotes, name='lista_filhotes'),
    path('administradores/', lista_administradores, name='lista_administradores'),
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
]
