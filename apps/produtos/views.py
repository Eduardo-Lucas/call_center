from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.produtos.models import Produto


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    fields = ['all', ]
    context_object_name = 'produto_list'
    template_name = 'produtos/produto_list.html'


class ProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Produto
    fields = '__all__'
    success_message = 'O Produto %(nome)s foi criado com sucesso.'


class ProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Produto
    fields = '__all__'
    success_message = 'O Produto %(nome)s foi atualizado com sucesso.'


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')
