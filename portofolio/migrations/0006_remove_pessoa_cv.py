# Generated by Django 4.2.2 on 2023-06-12 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0005_formresponses_pessoa_cv_pessoa_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='cv',
        ),
    ]