# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-10 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuxing', '0003_auto_20180910_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zb_type',
            name='zbb_type',
            field=models.CharField(max_length=50),
        ),
    ]
