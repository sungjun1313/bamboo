# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_auto_20180604_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack1',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pack2',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
