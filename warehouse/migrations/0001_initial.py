# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Define the supplier's name", max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(help_text='Choose the supplier or add one', on_delete=django.db.models.deletion.CASCADE, to='warehouse.Supplier')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name_plural': 'supplies',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(help_text='Specify the warehouse name', max_length=55)),
                ('address', models.TextField(help_text='Add address', max_length=255)),
            ],
        ),
    ]
