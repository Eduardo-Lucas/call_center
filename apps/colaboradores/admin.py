from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.colaboradores.models import Colaborador


@admin.register(Colaborador)
class ColaboradorResource(ImportExportModelAdmin):
    pass
