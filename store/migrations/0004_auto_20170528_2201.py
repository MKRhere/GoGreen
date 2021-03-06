# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20170528_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='lat',
            field=models.IntegerField(default=18.1124, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='store',
            name='lng',
            field=models.ImageField(default=79.0193, upload_to='', verbose_name='Longitude'),
        ),
    ]
