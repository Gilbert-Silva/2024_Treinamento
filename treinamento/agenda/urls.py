from django.urls import path
from .views import index, listar_clientes, inserir_cliente, editar_cliente

urlpatterns = [
    path('', index, name='index'),
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/inserir/', inserir_cliente, name='inserir_cliente'),
    path('clientes/editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
]


