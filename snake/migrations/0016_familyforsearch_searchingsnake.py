# Generated by Django 2.0.2 on 2018-04-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0015_delete_searchingsnake'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyForsearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SearchingSnake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_list', models.TextField(verbose_name="Liste d'espèces")),
            ],
        ),
    ]
