from django import forms

from apps.employee_register.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Nome Completo',
            'emp_code': 'Matrícula',
            'mobile': 'Telefone Celular',
            'position': 'Cargo'
        }

        def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select"

