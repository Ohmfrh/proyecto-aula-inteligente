# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
        ('usuarios', '0006_auto_20160426_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersys',
            name='songs',
            field=models.ManyToManyField(default=None, to='musica.Song'),
        ),
    ]
