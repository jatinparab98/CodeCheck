# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20170905_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
