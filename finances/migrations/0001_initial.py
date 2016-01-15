# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('currency', models.PositiveSmallIntegerField(choices=[(980, 'UAH'), (810, 'RUR'), (974, 'BYR'), (840, 'USD')])),
                ('type', models.PositiveIntegerField(choices=[(1, 'Cash'), (2, 'Cashless'), (3, 'Bank Card')])),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
        ),
    ]