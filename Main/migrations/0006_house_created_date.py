# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 11:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_house_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 12, 11, 55, 57, 116489, tzinfo=utc)),
        ),
    ]
