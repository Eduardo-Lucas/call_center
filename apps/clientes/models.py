from django.db import models
from django.urls import reverse

from apps.colaboradores.models import Colaborador
from apps.participantes.models import Participante


class Cliente(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True, help_text='Informe o CPF do Cliente')
    codigo = models.CharField(max_length=10, help_text='Informe o código do cliente')  # O cliente pode ter o mesmo código, porém em Participantes diferentes.
    nome = models.CharField(max_length=100, help_text='Informe o nome do cliente')  # O nome do cliente pode repetir para Participantes diferentes.
    telefone = models.CharField(max_length=20, default='(071) 9 9999-9999', help_text='Informe o telefone do cliente')
    email = models.EmailField(default='cliente@cliente.com.br', help_text='Informe o e-mail do cliente')
    cep = models.CharField(max_length=8, default=41000-000, help_text='Informe o CEP')
    endereco = models.CharField(max_length=50, default='Rua do Sobe e Desce',
                                help_text='Informe se é Rua, Avenida, etc')
    numero = models.CharField(max_length=10, default='s/n', help_text='Informe o número')
    complemento = models.CharField(max_length=10, blank=True, null=True, help_text='Informe o complemento')
    bairro = models.CharField(max_length=20, blank=True, null=True, help_text='Informe o bairro')
    cidade = models.CharField(max_length=20, default='Salvador', help_text='Informe a cidade')
    uf = models.CharField(max_length=2, default='BA', help_text='Informe o estado')
    pais = models.CharField(max_length=15, default='Brasil', help_text='Informe o país')

    def __str__(self):
        return self.nome

    class Meta:
        ordering: ['nome']
        unique_together: ['participante', 'codigo']

    @staticmethod
    def get_absolute_url():
        return reverse('cliente_list')
