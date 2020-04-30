from django.db import models
from django.urls import reverse

from apps.colaboradores.models import Colaborador


class Participante(models.Model):
    colaborador = models.ManyToManyField(Colaborador)
    cnpj = models.CharField(max_length=11, blank=True, null=True, help_text='Informe o CNPJ do Participante')
    codigo = models.CharField(max_length=15, unique=True)
    razao_social = models.CharField(max_length=100, unique=True)
    pessoa_contato = models.CharField(max_length=50, default='Fulano')
    telefone = models.CharField(max_length=20, default='(071) 9 9999-9999')
    email = models.EmailField(default='cliente@cliente.com.br')
    cep = models.CharField(max_length=8, default=41000 - 000, help_text='Informe o CEP')
    endereco = models.CharField(max_length=50, default='Rua do Sobe e Desce',
                                help_text='Informe se é Rua, Avenida, etc')
    numero = models.CharField(max_length=10, default='s/n', help_text='Informe o número')
    complemento = models.CharField(max_length=10, blank=True, null=True, help_text='Informe o complemento')
    bairro = models.CharField(max_length=50, blank=True, null=True, help_text='Informe o bairro',
                              default='Pituba')
    cidade = models.CharField(max_length=50, default='Salvador', help_text='Informe a cidade')
    uf = models.CharField(max_length=2, default='BA', help_text='Informe o estado')
    pais = models.CharField(max_length=15, default='Brasil', help_text='Informe o país')

    def __str__(self):
        return self.razao_social

    class Meta:
        ordering: ['razao_social']

    @staticmethod
    def get_absolute_url():
        return reverse('participante_list')
