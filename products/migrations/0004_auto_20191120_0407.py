# Generated by Django 2.1.14 on 2019-11-20 04:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191120_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='OEM_approved',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=3),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 20, 4, 7, 22, 246014)),
        ),
    ]
