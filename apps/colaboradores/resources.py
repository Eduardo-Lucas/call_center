from import_export import resources

from apps.colaboradores.models import Colaborador


class ColaboradorResource(resources.ModelResource):
    class Meta:
        model = Colaborador
        fields = ['all']
