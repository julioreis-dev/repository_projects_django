# Generated by Django 3.1.7 on 2021-02-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210224_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome_feature', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao_feature', models.TextField(max_length=200, verbose_name='descrição')),
                ('icone_feature', models.CharField(choices=[('lni-rocket', 'foguete'), ('lni-laptop-phone', 'laptop'), ('lni-cog', 'engrenagem'), ('lni-leaf', 'folhagem'), ('lni-layers', 'camadas')], max_length=50, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Característica',
                'verbose_name_plural': 'Características',
            },
        ),
    ]
