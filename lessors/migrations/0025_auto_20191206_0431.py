# Generated by Django 2.1.14 on 2019-12-06 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessors', '0024_auto_20191206_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessor',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 6, 4, 31, 7, 583884)),
        ),
    ]
