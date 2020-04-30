from django.urls import path

from apps.participantes.views import ParticipanteListView, ParticipanteCreateView, ParticipanteUpdateView, \
    ParticipanteDeleteView

urlpatterns = [
    path('list', ParticipanteListView.as_view(), name='participante_list'),
    path('create', ParticipanteCreateView.as_view(), name='participante_form'),
    path('edit/<pk>', ParticipanteUpdateView.as_view(), name='participante_edit'),
    path('delete/<pk>/', ParticipanteDeleteView.as_view(), name='participante_delete'),
]
