from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.colaboradores.models import Colaborador


class ColaboradorListView(LoginRequiredMixin, ListView):
    model = Colaborador
    fields = ['all', ]
    context_object_name = 'colaboradores_list'
    template_name = 'colaboradores/colaborador_list.html'


class ColaboradorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Colaborador
    fields = '__all__'
    success_message = 'O Colaborador %(nome)s foi criado com sucesso.'


class ColaboradorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Colaborador
    fields = '__all__'
    success_message = 'O Colaborador %(nome)s foi atualizado com sucesso.'


class ColaboradorDeleteView(LoginRequiredMixin, DeleteView):
    model = Colaborador
    success_url = reverse_lazy('colaborador_list')
