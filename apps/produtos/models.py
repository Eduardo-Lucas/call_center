from django.db import models
from django.urls import reverse

from apps.categorias.models import Categoria
from apps.participantes.models import Participante


class Produto(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    foto = models.ImageField(upload_to='produtos', blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=16, decimal_places=2)
    saldo = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        index_together = ('id', 'slug')

    def __str__(self):
        return self.nome

    @staticmethod
    def get_absolute_url():
        return reverse('produto_list')
