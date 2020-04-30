from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.clientes.models import Cliente


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    fields = ['all', ]
    context_object_name = 'cliente_list'
    template_name = 'clientes/cliente_list.html'


class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    fields = '__all__'
    success_message = 'O Cliente %(nome)s foi criado com sucesso.'


class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    success_message = 'O Cliente %(nome)s foi atualizado com sucesso.'


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
