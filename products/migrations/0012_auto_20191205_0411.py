# Generated by Django 2.1.14 on 2019-12-05 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20191205_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 5, 4, 11, 40, 326719)),
        ),
    ]
