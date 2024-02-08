from django.conf import settings
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('listar_agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('alterar_agendamento/<int:agendamento_id>/', views.alterar_agendamento, name='alterar_agendamento'),
    path('listar_servicos_precos/', views.listar_servicos_precos, name='listar_servicos_precos'),
    path('adicionar_servico_preco/', views.adicionar_servico_preco, name='adicionar_servico_preco'),
    path('modificar_servico_preco/<int:servico_id>/', views.modificar_servico_preco, name='modificar_servico_preco'),
    path('excluir_servico_preco/<int:servico_id>/', views.excluir_servico_preco, name='excluir_servico_preco'),
    path('cadastro_servicos_preco/', views.cadastro_servicos_preco, name='cadastro_servicos_preco'),     
    path('fazer_login/', auth_views.LoginView.as_view(), name='fazer_login'),    
    path('fazer_logout/', views.fazer_logout, name='fazer_logout'),   
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),    
    path('servicos_precos/', views.servicos_e_precos, name='servicos_e_precos'),
    path('meus_agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('login/', views.custom_login, name='custom_login'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
