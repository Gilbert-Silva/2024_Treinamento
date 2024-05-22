from django.urls import path
from .views import index, cliente_listar, cliente_inserir, cliente_editar, cliente_excluir

urlpatterns = [
    path('', index, name='index'),
    path('clientes/', cliente_listar, name='cliente_listar'),
    path('clientes/inserir/', cliente_inserir, name='cliente_inserir'),
    path('clientes/editar/<int:cliente_id>/', cliente_editar, name='cliente_editar'),
    path('clientes/excluir/<int:cliente_id>/', cliente_excluir, name='cliente_excluir'),
]


