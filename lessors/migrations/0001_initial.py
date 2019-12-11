# Generated by Django 2.1.14 on 2019-11-20 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect_id', models.CharField(max_length=400)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('joined_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 20, 3, 42, 17, 872414))),
            ],
        ),
    ]
