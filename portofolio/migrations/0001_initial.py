# Generated by Django 4.2.1 on 2023-06-09 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAptidao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoTecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ano_criacao', models.IntegerField()),
                ('link_oficial', models.URLField()),
                ('descricao', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.tipotecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('github', models.URLField(blank=True, null=True)),
                ('linguagens', models.ManyToManyField(to='portofolio.linguagem')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.tipoprojeto')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('universidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.universidade')),
            ],
        ),
        migrations.CreateModel(
            name='Interesses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ectsTotal', models.IntegerField()),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.professor')),
                ('universidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.universidade')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ects', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('anoEscolar', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.curso')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Aptidao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.pessoa')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portofolio.tipoaptidao')),
            ],
        ),
    ]
