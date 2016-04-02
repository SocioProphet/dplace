# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-02 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dplace_app', '0076_society_original_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='original_latitude',
            field=models.FloatField(null=True, verbose_name='ORIG_latitude'),
        ),
        migrations.AddField(
            model_name='society',
            name='original_longitude',
            field=models.FloatField(null=True, verbose_name='ORIG_longitude'),
        ),
    ]
