# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 23:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squawker',
            name='postdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='postdate'),
        ),
    ]
