# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headquarter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellpoint',
            name='warehouses',
            field=models.ManyToManyField(blank=True, to='warehouse.Warehouse'),
        ),
    ]