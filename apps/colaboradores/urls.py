from django.urls import path

from apps.colaboradores.views import ColaboradorCreateView, ColaboradorUpdateView, \
    ColaboradorDeleteView, ColaboradorListView

urlpatterns = [
    path('list', ColaboradorListView.as_view(), name='colaborador_list'),
    path('create', ColaboradorCreateView.as_view(), name='colaborador_form'),
    path('edit/<pk>', ColaboradorUpdateView.as_view(), name='colaborador_edit'),
    path('delete/<pk>/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),
    ]
