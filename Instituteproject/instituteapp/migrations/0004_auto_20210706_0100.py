# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-07-05 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
