# Generated by Django 2.1.14 on 2019-12-10 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessors', '0034_auto_20191210_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessor',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 10, 4, 3, 6, 21871)),
        ),
    ]
