# Generated by Django 4.2.1 on 2023-06-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0011_linguagem_acronimo_linguagem_ano_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linguagem',
            name='acronimo',
            field=models.CharField(default='wsl', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linguagem',
            name='ano_criacao',
            field=models.IntegerField(default=2012),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linguagem',
            name='criador',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='linguagem',
            name='imagem_exemplo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='linguagem',
            name='link_oficial',
            field=models.URLField(default='wsl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='linguagem',
            name='logotipo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
