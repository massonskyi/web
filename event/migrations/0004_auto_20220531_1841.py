# Generated by Django 2.1.15 on 2022-05-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.TimeField(),
        ),
    ]
