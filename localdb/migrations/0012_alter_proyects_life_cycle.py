# Generated by Django 3.2 on 2021-05-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localdb', '0011_alter_proyects_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyects',
            name='life_cycle',
            field=models.FloatField(),
        ),
    ]
