from django.urls import path

from apps.clientes.views import cliente_list, cliente_form, cliente_delete

urlpatterns = [
    path('list', cliente_list, name='cliente_list'),
    path('form', cliente_form, name='cliente_form'),
    path('delete', cliente_delete, name='cliente_delete'),
    ]
