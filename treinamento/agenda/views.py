from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from agenda.models import Cliente, Servico
from agenda.forms import ClienteForm, ServicoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # Number of visits to this view, as counted in the session variable.
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1

    contexto = {
        'visits': visits,
    }    

    #return render(request, 'index.html')
    return render(request, 'index.html', context = contexto)

@login_required
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

@login_required
def servico_listar(request):
    servicos = Servico.objects.all()
    return render(request, 'servico_listar.html', {'servicos': servicos})

def servico_inserir(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_listar')
        else:
            messages.error(request, "Informe os dados corretamente!")
            return redirect('servico_inserir')
    else:
        form = ServicoForm()
    return render(request, 'servico_inserir.html', {'form': form })

def servico_editar(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_listar')
        else:
            messages.error(request, "Informe os dados corretamente!")
            return redirect('servico_editar')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servico_editar.html', {'form': form})

def servico_excluir(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_listar')
    return render(request, 'servico_excluir.html', {'servico': servico})
