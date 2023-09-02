# Generated by Django 4.1.7 on 2023-07-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_reserva_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('creada', 'Creada'), ('espera_aprobacion', 'Espera de Aprobación'), ('aprobada', 'Aprobada'), ('en_proceso', 'En Proceso'), ('finalizada', 'Finalizada'), ('pagada', 'Pagada')], default='creada', max_length=20),
        ),
    ]