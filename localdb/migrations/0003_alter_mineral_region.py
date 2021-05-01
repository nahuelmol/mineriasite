# Generated by Django 3.2 on 2021-04-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localdb', '0002_auto_20210423_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='region',
            field=models.TextField(blank=None, choices=[(1, 'Region Occidental'), (2, 'Region Central'), (3, 'Region Oriental')], default='who_cares', max_length=40),
        ),
    ]