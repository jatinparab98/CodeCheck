# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-30 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20170905_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
