from import_export import resources

from apps.categorias.models import Categoria


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        fields = ['all']
