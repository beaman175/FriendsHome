# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-05 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20170805_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
