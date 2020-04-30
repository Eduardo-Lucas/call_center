from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente


@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'participantes/participante_list.html', {'participantes': clientes})


@login_required
def cliente_form(request):
    form = ClienteForm()
    return render(request, 'participantes/participante_form.html', {'form': form})


@login_required
def cliente_delete(request):
    pass
    # return render(request, 'participantes/participante_delete.html')
