from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.employee_register.models import Position, Employee


@admin.register(Position)
class PositionResource(ImportExportModelAdmin):
    pass


@admin.register(Employee)
class EmployeeResource(ImportExportModelAdmin):
    pass
