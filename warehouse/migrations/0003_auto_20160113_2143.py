# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20160113_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyitem',
            name='supply',
            field=models.ForeignKey(blank=True, help_text='Add related supply', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Supply'),
        ),
    ]