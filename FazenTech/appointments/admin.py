from django.contrib import admin
from .models import Vacas, RegistroLeite, Filhote, Administrador, Funcionarios

admin.site.register(Vacas)
admin.site.register(RegistroLeite)
admin.site.register(Filhote)
admin.site.register(Administrador)
admin.site.register(Funcionarios)

