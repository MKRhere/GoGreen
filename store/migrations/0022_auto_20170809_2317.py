# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20170809_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('F', 'Franchise'), ('S', 'Store')], max_length=1),
        ),
    ]