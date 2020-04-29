from import_export import resources

from apps.clientes.models import Cliente


class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        fields = ['all']
