# Generated by Django 4.0.5 on 2022-06-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20220531_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
