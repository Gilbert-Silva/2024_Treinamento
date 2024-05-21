from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from agenda.models import Cliente
from agenda.forms import ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def inserir_cliente(request):
    #invalido = False
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
        else:
            messages.error(request, "Informe os dados corretamente!")
            #invalido = True
            return redirect('inserir_cliente')
    else:
        form = ClienteForm()
    #return render(request, 'inserir_cliente.html', {'form': form, 'invalido' : invalido })
    return render(request, 'inserir_cliente.html', {'form': form })

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # Lógica para remover o cliente
    cliente.delete()
    return redirect('listar_clientes')
