# Generated by Django 2.1.14 on 2019-12-08 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessees', '0009_auto_20191208_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessee',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 8, 4, 29, 28, 76146)),
        ),
    ]