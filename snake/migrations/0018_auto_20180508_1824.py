# Generated by Django 2.0.2 on 2018-05-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0017_auto_20180416_2216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchingsnake',
            options={'verbose_name': 'Espèces recherchées', 'verbose_name_plural': 'Espèces recherchées'},
        ),
        migrations.AlterField(
            model_name='salingsnake',
            name='scientific_name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
    ]
