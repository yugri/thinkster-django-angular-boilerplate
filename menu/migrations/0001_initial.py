# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Specify ingredient/product name', max_length=128)),
                ('sku', models.CharField(help_text='Stock Keeping Unit', max_length=50)),
                ('measure_units', models.CharField(choices=[('l', 'liter'), ('kg', 'kilogram'), ('box', 'box'), ('set', 'set')], help_text='Choose the measure units', max_length=5)),
            ],
        ),
    ]