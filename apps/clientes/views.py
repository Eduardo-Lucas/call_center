from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente


@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})


@login_required
def cliente_form(request):
    form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})


@login_required
def cliente_delete(request):
    pass
    # return render(request, 'clientes/cliente_delete.html')
