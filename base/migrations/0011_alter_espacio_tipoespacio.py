# Generated by Django 4.1.7 on 2023-05-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_espacio_tipoespacio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='tipoEspacio',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Arte', 'Arte'), ('ArtMarcial', 'ArtMarcial'), ('Cocina', 'Cocina'), ('Danza', 'Danza'), ('Musica', 'Musica'), ('Gimnasio', 'Gimnasio'), ('Fotografia', 'Fotografia'), ('Showroom', 'Showroom'), ('Otros', 'Otros')], max_length=15),
        ),
    ]