# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-07-05 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0002_coursedata_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('datetime', models.DateField(auto_now_add=True)),
                ('feedback', models.TextField(max_length=100)),
            ],
        ),
    ]