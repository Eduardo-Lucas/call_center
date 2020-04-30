from import_export import resources

from apps.participantes.models import Participante


class ParticipanteResource(resources.ModelResource):
    class Meta:
        model = Participante
        fields = ['all']
