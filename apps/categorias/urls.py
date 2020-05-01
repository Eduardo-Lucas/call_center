from django.urls import path

from apps.categorias.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

urlpatterns = [
    path('list', CategoriaListView.as_view(), name='categoria_list'),
    path('create', CategoriaCreateView.as_view(), name='categoria_form'),
    path('edit/<pk>', CategoriaUpdateView.as_view(), name='categoria_edit'),
    path('delete/<pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
]
