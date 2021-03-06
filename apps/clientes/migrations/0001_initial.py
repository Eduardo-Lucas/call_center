# Generated by Django 3.0.5 on 2020-04-30 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, help_text='Informe o CPF do Cliente', max_length=11, null=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(default='(071) 9 9999-9999', max_length=20)),
                ('email', models.EmailField(default='cliente@cliente.com.br', max_length=254)),
                ('cep', models.CharField(default=41000, help_text='Informe o CEP', max_length=8)),
                ('endereco', models.CharField(default='Rua do Sobe e Desce', help_text='Informe se é Rua, Avenida, etc', max_length=50)),
                ('numero', models.CharField(default='s/n', help_text='Informe o número', max_length=10)),
                ('complemento', models.CharField(blank=True, help_text='Informe o complemento', max_length=10, null=True)),
                ('bairro', models.CharField(blank=True, help_text='Informe o bairro', max_length=20, null=True)),
                ('cidade', models.CharField(default='Salvador', help_text='Informe a cidade', max_length=20)),
                ('uf', models.CharField(default='BA', help_text='Informe o estado', max_length=2)),
                ('pais', models.CharField(default='Brasil', help_text='Informe o país', max_length=15)),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participantes.Participante')),
            ],
        ),
    ]
