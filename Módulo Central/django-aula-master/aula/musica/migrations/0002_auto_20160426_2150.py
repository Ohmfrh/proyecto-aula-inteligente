# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='musica.Song'),
        ),
    ]
