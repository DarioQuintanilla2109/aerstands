# Generated by Django 2.1.14 on 2019-12-05 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessors', '0010_auto_20191205_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessor',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 5, 3, 56, 44, 512363)),
        ),
    ]
