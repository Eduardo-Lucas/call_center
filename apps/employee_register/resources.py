from import_export import resources

from apps.employee_register.models import Position, Employee


class PositionResource(resources.ModelResource):
    class Meta:
        model = Position
        fields = ['all']


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        fields = ['all']
