# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 16:38
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
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
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media/products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
    ]
