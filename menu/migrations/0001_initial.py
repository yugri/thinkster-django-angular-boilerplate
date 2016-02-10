# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Specify product/ingredient name', max_length=128)),
                ('type', models.CharField(choices=[('good', 'Good'), ('ingredient', 'Ingredient'), ('service', 'Service')], max_length=50, null=True)),
                ('sku', models.CharField(blank=True, help_text='Stock Keeping Unit', max_length=50)),
                ('measure_units', models.CharField(blank=True, choices=[('pcs.', 'pieces'), ('l', 'liter'), ('kg', 'kilogram'), ('box', 'box'), ('set', 'set')], help_text='Choose the measure units', max_length=5, null=True)),
            ],
        ),
    ]
