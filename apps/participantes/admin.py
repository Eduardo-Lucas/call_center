from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.participantes.models import Participante


@admin.register(Participante)
class ParticipanteResource(ImportExportModelAdmin):
    pass
