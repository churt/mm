# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20180306_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseclient',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='baseclient',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
