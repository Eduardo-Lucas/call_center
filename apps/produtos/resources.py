from import_export import resources

from apps.produtos.models import Produto


class ProdutoResource(resources.ModelResource):
    class Meta:
        model = Produto
        fields = ['all']
