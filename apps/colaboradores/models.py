from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Colaborador(models.Model):
    """Manutenção do Cadastro de Colaboradores"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    call_center = models.BooleanField(default=False, help_text='Se marcado, indica que trabalha no Call Center')
    # Auto relacionamento: um gerente pode ter um ou mais colaboradores
    gerente = models.ForeignKey('self', null=True, blank=True, related_name='colaborador', on_delete=models.CASCADE)

    nome = models.CharField(max_length=100, help_text='Nome do colaborador')
    telefone = models.CharField(max_length=20, help_text='Informe o número de telefone')
    email = models.EmailField(max_length=30, blank=True, null=True, help_text='Email do colaborador')

    def is_call_center(self):
        if self.call_center:
            return 'Sim'
        else:
            return 'Não'

    def __str__(self):
        return self.nome + ' trabalha no Call Center = ' + self.is_call_center()

    @staticmethod
    def get_absolute_url():
        return reverse('colaborador_list')
