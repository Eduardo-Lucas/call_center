from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.categorias.models import Categoria


@admin.register(Categoria)
class CategoriaResource(ImportExportModelAdmin):
    pass
