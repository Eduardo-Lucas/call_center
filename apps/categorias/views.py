from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.categorias.models import Categoria


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    fields = ['all', ]
    context_object_name = 'categoria_list'
    template_name = 'categorias/categoria_list.html'


class CategoriaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    fields = '__all__'
    success_message = 'O Categoria %(nome)s foi criado com sucesso.'


class CategoriaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    fields = '__all__'
    success_message = 'O Categoria %(nome)s foi atualizado com sucesso.'


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
