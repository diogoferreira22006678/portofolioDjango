# Generated by Django 4.2.1 on 2023-06-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0014_escola_logo_universidade_fim_universidade_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='interesses/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
