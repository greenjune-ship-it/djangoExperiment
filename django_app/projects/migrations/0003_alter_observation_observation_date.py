# Generated by Django 5.0 on 2023-12-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_observation_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='observation_date',
            field=models.DateField(),
        ),
    ]
