from django import forms
from .models import Vacas, RegistroLeite, Filhote, Administrador, Funcionarios

class VacasForm(forms.ModelForm):
    class Meta:
        model = Vacas
        fields = '__all__'

class RegistroLeiteForm(forms.ModelForm):
    class Meta:
        model = RegistroLeite
        fields = '__all__'

class FilhoteForm(forms.ModelForm):
    class Meta:
        model = Filhote
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = '__all__'
