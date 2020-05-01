from django.db import models

from apps.categorias.models import Categoria


class Produto(models.Model):
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


