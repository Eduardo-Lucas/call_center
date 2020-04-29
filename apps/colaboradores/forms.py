from django import forms
from apps.colaboradores.models import Colaborador


class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = '__all__'
