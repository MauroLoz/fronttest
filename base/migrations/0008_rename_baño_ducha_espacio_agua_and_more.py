# Generated by Django 4.1.7 on 2023-05-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_espacio_direccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espacio',
            old_name='baño_ducha',
            new_name='agua',
        ),
        migrations.RenameField(
            model_name='espacio',
            old_name='espejos',
            new_name='aire',
        ),
        migrations.AddField(
            model_name='espacio',
            name='calefaccion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='espacio',
            name='lineaTelefonica',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='espacio',
            name='techo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='espacio',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
    ]
