# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 21:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_house_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 21, 7, 48, 449387)),
        ),
    ]
