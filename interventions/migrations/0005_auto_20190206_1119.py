# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0004_auto_20180808_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='description',
            field=models.TextField(blank=True, verbose_name='Geef een beschrijving van de experimentele interventie'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Wat is de duur van de interventie per sessie in minuten?'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='experimenter',
            field=models.TextField(blank=True, verbose_name='Wie voert de interventie uit? Leg uit wat de rol en de functie van de persoon is. '),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='measurement',
            field=models.TextField(blank=True, help_text='Wanneer u de deelnemer extra taken laat uitvoeren, dus een taak die niet behoort tot het reguliere onderwijspakket, dan moet u op de vorige pagina ook "takenonderzoek" aanvinken.', verbose_name='Hoe wordt het effect van de interventie gemeten?'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='period',
            field=models.TextField(blank=True, help_text='Geef aan wanneer de interventie plaatsvindt. Bijvoorbeeld binnen het schooljaar 2022-2023', verbose_name='Wat is de periode waarbinnen de interventie plaatsvindt?'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='setting',
            field=models.ManyToManyField(blank=True, to='main.Setting', verbose_name='Geef aan waar de dataverzameling plaatsvindt'),
        ),
    ]
