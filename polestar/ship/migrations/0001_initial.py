# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('imo_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
    ]
