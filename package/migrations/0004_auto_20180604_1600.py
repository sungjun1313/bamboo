# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_auto_20180604_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack1',
            name='custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='package.Custom'),
        ),
        migrations.AlterField(
            model_name='pack2',
            name='custom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='package.Custom'),
        ),
    ]
