# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 00:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20160430_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersys',
            name='date_added',
            field=models.DateField(default=datetime.date(2016, 5, 1), verbose_name='Fecha de alta'),
        ),
    ]
