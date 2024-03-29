# Generated by Django 2.1.14 on 2019-12-07 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessors', '0028_auto_20191207_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessor',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 7, 20, 17, 58, 836201)),
        ),
        migrations.AlterField(
            model_name='lessor',
            name='photo',
            field=models.ImageField(blank=True, default='img/avatar.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
