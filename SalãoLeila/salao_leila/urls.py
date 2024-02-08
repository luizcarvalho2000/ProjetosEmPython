from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointments import views as appointments_views, views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('', appointments_views.pagina_inicial, name='pagina_inicial'),  # Rota para a página inicial
    path('fazer_login/', appointments_views.fazer_login, name='fazer_login'),
    path('registrar_usuario/', appointments_views.registrar_usuario, name='registrar_usuario'),
    path('listar_agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('fazer_logout/', appointments_views.fazer_logout, name='fazer_logout'),
    path('fazer_login/', auth_views.LoginView.as_view(), name='fazer_login'),
    path('servicos_precos/', views.servicos_e_precos, name='servicos_e_precos'),
    path('listar_servicos_precos/', views.listar_servicos_precos, name='listar_servicos_precos'),
    path('adicionar_servico_preco/', views.adicionar_servico_preco, name='adicionar_servico_preco'),
    path('cadastro_servicos_preco/', views.cadastro_servicos_preco, name='cadastro_servicos_preco'),
    path('modificar_servico_preco/<int:servico_id>/', views.modificar_servico_preco, name='modificar_servico_preco'),
    path('excluir_servico_preco/<int:servico_id>/', views.excluir_servico_preco, name='excluir_servico_preco'),
    path('meus_agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('login/', views.custom_login, name='custom_login'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
