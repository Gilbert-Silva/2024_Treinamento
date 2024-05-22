from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from agenda.models import Cliente
from agenda.forms import ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cliente_listar(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_listar.html', {'clientes': clientes})

def cliente_inserir(request):
    #invalido = False
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_listar')
        else:
            messages.error(request, "Informe os dados corretamente!")
            #invalido = True
            return redirect('cliente_inserir')
    else:
        form = ClienteForm()
    #return render(request, 'inserir_cliente.html', {'form': form, 'invalido' : invalido })
    return render(request, 'cliente_inserir.html', {'form': form })

def cliente_editar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_listar')
        else:
            messages.error(request, "Informe os dados corretamente!")
            return redirect('cliente_editar')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_editar.html', {'form': form})

def cliente_excluir(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_listar')
    return render(request, 'cliente_excluir.html', {'cliente': cliente})
    
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # Lógica para remover o cliente
    cliente.delete()
    return redirect('cliente_listar')
