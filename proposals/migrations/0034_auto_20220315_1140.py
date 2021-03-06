# Generated by Django 2.2.24 on 2022-03-15 10:40

from django.db import migrations, models
import django.db.models.deletion
import main.validators
import proposals.utils.proposal_utils
import proposals.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0033_auto_20210521_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='avg_understood',
            field=models.BooleanField(default=False, validators=[proposals.validators.AVGUnderstoodValidator], verbose_name='Ik heb kennis genomen van het bovenstaande en begrijp mijn verantwoordelijkheden ten opzichte van de AVG.'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='dmp_file',
            field=models.FileField(blank=True, storage=proposals.utils.proposal_utils.OverwriteStorage(), upload_to=proposals.utils.proposal_utils.FilenameFactory('DMP'), validators=[main.validators.validate_pdf_or_doc], verbose_name='Als je een Data Management Plan heeft voor deze studie, kunt u kiezen om deze hier bij te voegen. Het aanleveren van een DMP vergemakkelijkt het toetsingsproces aanzienlijk.'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proposals.Institution', verbose_name='Aan welke organisatie bent u verbonden?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='other_stakeholders',
            field=models.BooleanField(default=False, verbose_name='Zijn er nog andere onderzoekers bij deze studie betrokken die <strong>niet</strong> geaffilieerd zijn aan een van bovengenoemde organisaties?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='title',
            field=models.CharField(help_text='De titel die u hier opgeeft is zichtbaar voor de Deelkracht-leden en, wanneer de studie is goedgekeurd, ook voor alle medewerkers die in het archief van deze portal kijken. De titel mag niet identiek zijn aan een vorige titel van een studie die u heeft ingediend.', max_length=200, verbose_name='Wat is de titel van uw studie? Deze titel zal worden gebruikt in alle formele correspondentie.'),
        ),
        migrations.AlterField(
            model_name='wmo',
            name='metc',
            field=models.CharField(blank=True, choices=[('Y', 'ja'), ('N', 'nee'), ('?', 'twijfel')], default=None, max_length=1, verbose_name='Vindt de dataverzameling plaats binnen het UMC Utrecht of andere instelling waar toetsing door een METC verplicht is gesteld?'),
        ),
    ]
