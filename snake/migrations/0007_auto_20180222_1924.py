# Generated by Django 2.0.2 on 2018-02-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0006_auto_20180222_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snake',
            name='venom',
            field=models.ManyToManyField(blank=True, to='snake.Venom'),
        ),
    ]
