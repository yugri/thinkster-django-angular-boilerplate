# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20160307_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trans_type',
            field=models.CharField(choices=[(1, 'Revenue'), (2, 'Waste'), (3, 'Transfer')], max_length=24),
        ),
    ]
