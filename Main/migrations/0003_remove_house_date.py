# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-05 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20170805_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='date',
        ),
    ]