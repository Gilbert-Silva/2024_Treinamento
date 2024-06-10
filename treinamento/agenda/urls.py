from django.urls import path
from .views import index, cliente_listar, cliente_inserir, cliente_editar, cliente_excluir, servico_listar, servico_inserir, servico_editar, servico_excluir

urlpatterns = [
    path('', index, name='index'),
    path('clientes/', cliente_listar, name='cliente_listar'),
    path('clientes/inserir/', cliente_inserir, name='cliente_inserir'),
    path('clientes/editar/<int:cliente_id>/', cliente_editar, name='cliente_editar'),
    path('clientes/excluir/<int:cliente_id>/', cliente_excluir, name='cliente_excluir'),
    path('servicos/', servico_listar, name='servico_listar'),
    path('servicos/inserir/', servico_inserir, name='servico_inserir'),
    path('servicos/editar/<int:servico_id>/', servico_editar, name='servico_editar'),
    path('servicos/excluir/<int:servico_id>/', servico_excluir, name='servico_excluir'),
]


