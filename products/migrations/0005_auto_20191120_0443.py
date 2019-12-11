# Generated by Django 2.1.14 on 2019-11-20 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191120_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=7),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 20, 4, 43, 50, 290343)),
        ),
    ]
