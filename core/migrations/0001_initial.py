# Generated by Django 3.1.5 on 2021-02-03 17:47

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criacao')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Data de Atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preco')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
                ('imagem', stdimage.models.StdImageField(upload_to='produtos', verbose_name='imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
