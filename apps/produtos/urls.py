from django.urls import path

from apps.produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('list', ProdutoListView.as_view(), name='produto_list'),
    path('create', ProdutoCreateView.as_view(), name='produto_form'),
    path('edit/<pk>', ProdutoUpdateView.as_view(), name='produto_edit'),
    path('delete/<pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
