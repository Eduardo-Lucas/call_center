from django.urls import path

from apps.clientes.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('list', ClienteListView.as_view(), name='cliente_list'),
    path('create', ClienteCreateView.as_view(), name='cliente_form'),
    path('edit/<pk>', ClienteUpdateView.as_view(), name='cliente_edit'),
    path('delete/<pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
