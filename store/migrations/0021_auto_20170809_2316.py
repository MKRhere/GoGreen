# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20170809_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='franchise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='franchise_product', to='store.Franchise'),
        ),
    ]
