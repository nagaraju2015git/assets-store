# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetclass',
            name='acdetails',
            field=models.CharField(default='Details', max_length=35),
            preserve_default=False,
        ),
    ]
