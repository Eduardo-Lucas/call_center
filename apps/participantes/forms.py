from django.forms import forms

from apps.participantes.models import Participante


class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = '__all__'

