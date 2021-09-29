# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-12-03 08:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0022_auto_20191107_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='applicants',
            field=models.ManyToManyField(help_text='Klik in het vlak hiernaast en type een aantal letters van de voornaam, achternaam, of Solis ID van             de persoon die u toe wilt voegen. Klik vervolgens om de persoon toe te voegen. Merk op dat het laden even kan duren.', related_name='applicants', to=settings.AUTH_USER_MODEL, verbose_name='Uitvoerende(n) (inclusief uzelf)'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='supervisor',
            field=models.ForeignKey(blank=True, help_text='Aan het einde van de procedure kunt u deze studie ter verificatie naar uw eindverantwoordelijke\n            sturen. De eindverantwoordelijke zal de studie vervolgens kunnen aanpassen en indienen bij de FETC-GW.\n            <br><br><strong>Tip</strong>: Type een aantal letters van de voornaam, achternaam, of Solis ID van\n            de persoon die u toe wilt voegen in de zoekbalk hiernaast. Merk op dat het laden even kan duren.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Eindverantwoordelijke onderzoeker'),
        ),
    ]
