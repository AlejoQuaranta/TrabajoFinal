# Generated by Django 4.0.4 on 2022-06-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='cellphone',
            field=models.IntegerField(unique=True),
        ),
    ]
