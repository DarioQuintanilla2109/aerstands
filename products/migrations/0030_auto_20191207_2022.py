# Generated by Django 2.1.14 on 2019-12-07 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20191207_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 7, 20, 22, 19, 70738)),
        ),
    ]