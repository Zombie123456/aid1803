# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-10 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuxing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zb_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shouzhu', models.IntegerField()),
                ('xianglian', models.IntegerField()),
                ('toukui', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='zhuangbei',
            name='z_type',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
