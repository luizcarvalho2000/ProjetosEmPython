from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Agendamento, Servico, Cliente, Preco
from .forms import AgendamentoForm, AlterarAgendamentoForm, RegistroForm, LoginForm, ServicoForm, PrecoForm

def is_admin(user):
    return user.is_superuser

def custom_login(request):
    return render(request, 'admin/login.html')

def fazer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireciona para a página inicial ou outra página após o login bem-sucedido
            return redirect('pagina_inicial')
        else:
            # Trate o caso de credenciais de login inválidas aqui
            pass
    # Renderiza o formulário de login
    return render(request, 'registration/login.html')

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Salva o novo usuario no banco de dados
            user = form.save(commit=False)
            # Cria um novo cliente para o usuário
            cliente = Cliente.objects.create(user=user, nome=user.username, telefone='')            
            
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso.')

            # Cria um agendamento para o cliente            
            #Agendamento.objects.create(cliente=cliente, data_hora='2020-01-01 00:00:00', servicos=Servico.objects.get(id=1))
            
            return redirect('pagina_inicial')  # Redireciona após o registro bem-sucedido
    else:
        form = RegistroForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required
def fazer_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('pagina_inicial')

@login_required
@user_passes_test(is_admin)
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'listar_agendamentos.html', {'agendamentos': agendamentos})

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            # Salva o agendamento no banco de dados
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user.cliente  
            agendamento.save()
            messages.success(request, 'Agendamento realizado com sucesso.')
            return redirect('meus_agendamentos.html')
        else:
            # Verifique se a data/hora já estão em uso
            data_hora = form.cleaned_data['data_hora']
            if Agendamento.objects.filter(data_hora=data_hora).exists():
                form.add_error('data_hora', 'Este horário já está agendado.')
            
            else:return redirect('meus_agendamentos.html')

    else:
        form = AgendamentoForm()

    return render(request, 'criar_agendamento.html', {'form': form})



def alterar_agendamento(request, agendamento_id):
    agendamento = Agendamento.objects.get(pk=agendamento_id)
    if request.method == 'POST':
        form = AlterarAgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento alterado com sucesso.')
            return redirect('listar_agendamentos')
    else:
        form = AlterarAgendamentoForm(instance=agendamento)
    
    return render(request, 'appointments/alterar_agendamento.html', {'agendamento': agendamento})

@login_required
def meus_agendamentos(request):
    agendamentos = []
    if hasattr(request.user, 'cliente'):
        user = request.user.cliente
        agendamentos = Agendamento.objects.filter(cliente=user).select_related('cliente', 'servicos')
        return render(request, 'meus_agendamentos.html', {'agendamentos': agendamentos})
    else:
        return render(request, 'meus_agendamentos.html', {'agendamentos': agendamentos})
    

@login_required
def servicos_e_precos(request):
    servicos = Servico.objects.all()
    
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        preco_form = PrecoForm(request.POST)
        
        if servico_form.is_valid() and preco_form.is_valid():
            servico_form.save()
            preco_form.save()
            return redirect('servicos_e_precos')
    else:
        servico_form = ServicoForm()
        preco_form = PrecoForm()
    
    return render(request, 'servicos_precos.html', {'servicos': servicos, 'servico_form': servico_form, 'preco_form': preco_form})

@login_required
def listar_servicos_precos(request):
    servicos_precos = Servico.objects.all()
    return render(request, 'listar_servicos_precos.html', {'servicos_precos': servicos_precos})

@login_required
def adicionar_servico_preco(request):
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        preco_form = PrecoForm(request.POST)
        if servico_form.is_valid() and preco_form.is_valid():
            servico = servico_form.save()
            preco = preco_form.save(commit=False)
            preco.servico = servico
            preco.save()
            return redirect('listar_servicos_precos')
    else:
        servico_form = ServicoForm()
        preco_form = PrecoForm()
    
    return render(request, 'adicionar_servico_preco.html', {'servico_form': servico_form, 'preco_form': preco_form})

@staff_member_required
def modificar_servico_preco(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    preco = Preco.objects.get(servico=servico)  
    
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST, instance=servico)
        preco_form = PrecoForm(request.POST, instance=preco)
        
        if servico_form.is_valid() and preco_form.is_valid():
            servico_form.save()
            preco_form.save()
            return redirect('listar_servicos_precos')
    else:
        servico_form = ServicoForm(instance=servico)
        preco_form = PrecoForm(instance=preco)
    
    return render(request, 'modificar_servico_preco.html', {'servico_form': servico_form, 'preco_form': preco_form})


@staff_member_required
def excluir_servico_preco(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    if request.method == 'POST':
        servico.delete()
        return redirect('listar_servicos_precos')
    
    return render(request, 'excluir_servico_preco.html', {'servico': servico})

@staff_member_required
def cadastro_servicos_preco(request):
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        preco_form = PrecoForm(request.POST)
        
        if servico_form.is_valid() and preco_form.is_valid():
            servico = servico_form.save()
            preco = preco_form.save(commit=False)
            preco.servico = servico
            preco.save()
            return redirect('listar_servicos_precos')
    else:
        servico_form = ServicoForm()
        preco_form = PrecoForm()
    
    return render(request, 'cadastro_servicos_preco.html', {'servico_form': servico_form, 'preco_form': preco_form})


def pagina_inicial(request):
    return render(request, 'index.html')
