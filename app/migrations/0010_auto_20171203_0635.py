# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-03 06:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20161229_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2017, 12, 3, 6, 35, 49, 501956)),
        ),
    ]