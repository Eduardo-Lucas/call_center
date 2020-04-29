from django import forms

from apps.clientes.models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'colaborador': 'Colaborador responsável por esse Cliente',
            'codigo': 'Código do Cliente',
        }
