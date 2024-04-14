# Generated by Django 4.2.4 on 2024-04-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes_aqp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='capacidad',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='horario_apertura',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='horario_cierre',
            field=models.TimeField(default='23:59'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='tiene_entrega_domicilio',
            field=models.BooleanField(default=False),
        ),
    ]
