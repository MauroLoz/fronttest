# Generated by Django 4.1.7 on 2023-06-03 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='tipoEspacio',
            new_name='tipoGenero',
        ),
    ]
