from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models import Avg
from datetime import datetime
from django.utils import timezone


class Vacas(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(help_text="Idade em anos")
    peso = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    leite_diario = models.DecimalField(max_digits=10, decimal_places=4, default=Decimal('0.00'))
    numero_de_crias = models.IntegerField(default=0)
    esta_prenha = models.BooleanField(default=False)
    esta_amamentando = models.BooleanField(default=False)
    esta_no_cio = models.BooleanField(default=False)
    esta_doente = models.BooleanField(default=False)
    semana_de_gestacao = models.IntegerField(default=0)    
    ultima_inseminacao = models.DateTimeField(null=True, blank=True)
    ultima_paricao = models.DateTimeField(null=True, blank=True)
    ultima_pesagem = models.DateTimeField(null=True, blank=True)
    ultima_vacinacao = models.DateTimeField(null=True, blank=True)
    ultima_vermifugacao = models.DateTimeField(null=True, blank=True)

def media_leite_mensal(self):
    registros_do_mes = self.registroleite_set.filter(data__month=datetime.now().month)
    media_leite = registros_do_mes.aggregate(Avg('quantidade'))['quantidade__avg']
    return media_leite

def __str__(self):
    return self.nome

class RegistroLeite(models.Model):
    vaca = models.ForeignKey('Vacas', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=4, default=Decimal('0.00'))

class Filhote(models.Model):
    mae = models.ForeignKey('Vacas', on_delete=models.CASCADE)
    numero = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(help_text="Idade em anos")
    peso = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

class Funcionarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    funcao = models.CharField(max_length=100)        
    esta_trabalhando = models.BooleanField(default=True)

