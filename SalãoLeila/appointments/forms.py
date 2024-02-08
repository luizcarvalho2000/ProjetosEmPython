from django import forms
from .models import Servico, Cliente, Preco, Agendamento
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone

class AgendamentoForm(forms.ModelForm):
    servicos = forms.ModelMultipleChoiceField(
        queryset=Servico.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
    )
    
    preco = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Agendamento
        fields = ['cliente', 'servicos', 'data_hora', 'alteravel']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_data_hora(self):
        data_hora = self.cleaned_data['data_hora']
        if Agendamento.objects.filter(data_hora=data_hora).exists():
            raise forms.ValidationError('Este horário já está agendado.')
        elif data_hora < timezone.now():
            raise forms.ValidationError('A data/hora não pode ser anterior à data/hora atual.')
        return data_hora

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['cliente'].initial = user.cliente
    
class AlterarAgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servicos', 'data_hora', 'confirmado']

class RegistroForm(UserCreationForm):
    email = forms.EmailField() 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['servico', 'duracao']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone']

class PrecoForm(forms.ModelForm):
    class Meta:
        model = Preco
        fields = ['servico', 'valor']
