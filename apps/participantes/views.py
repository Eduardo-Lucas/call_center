from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.participantes.models import Participante


class ParticipanteListView(LoginRequiredMixin, ListView):
    model = Participante
    fields = ['all', ]
    context_object_name = 'participantes_list'
    template_name = 'participantes/participante_list.html'


class ParticipanteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Participante
    fields = '__all__'
    success_message = 'O Participante %(razao_social)s foi criado com sucesso.'


class ParticipanteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Participante
    fields = '__all__'
    success_message = 'O Participante %(razao_social)s foi atualizado com sucesso.'


class ParticipanteDeleteView(LoginRequiredMixin, DeleteView):
    model = Participante
    success_url = reverse_lazy('participante_list')
