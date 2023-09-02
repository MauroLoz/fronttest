# Generated by Django 4.1.7 on 2023-06-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_espacio_tipoespacio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='tipoEspacio',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Arte', 'Arte'), ('ArtMarcial', 'ArtMarcial'), ('Cocina', 'Cocina'), ('Danza', 'Danza'), ('Musica', 'Musica'), ('Gimnasio', 'Gimnasio'), ('Fotografía', 'Fotografía'), ('Showroom', 'Showroom'), ('Otros', 'Otros')], max_length=15),
        ),
    ]