# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_auto_20160307_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='fincategory',
            name='apply_revenues',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fincategory',
            name='apply_wastes',
            field=models.BooleanField(default=True),
        ),
    ]
