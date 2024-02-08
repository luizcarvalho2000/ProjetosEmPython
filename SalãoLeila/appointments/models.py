from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils import timezone



class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome

class Preco(models.Model):
    servico = models.OneToOneField('Servico', on_delete=models.CASCADE, related_name='precos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Preço de {self.servico} - R${self.valor}"

class Servico(models.Model):
    servico = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField(help_text="Duração em minutos")
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.servico

class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico, blank=True)
    data_hora = models.DateTimeField(null=True, blank=True)
    confirmado = models.BooleanField(default=False)
    alteravel = models.BooleanField(default=True)

    def __str__(self):
        return f"Agendamento de {self.cliente} em {self.data_hora}"

