# Generated by Django 3.2 on 2021-05-03 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localdb', '0010_alter_proyects_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyects',
            name='region',
            field=models.TextField(blank=True, default='Around there'),
        ),
    ]