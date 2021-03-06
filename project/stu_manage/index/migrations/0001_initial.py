# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-05 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sclass', models.CharField(max_length=10, verbose_name='班')),
                ('grade', models.CharField(max_length=10, verbose_name='年级')),
            ],
            options={
                'verbose_name_plural': '年级',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('snum', models.CharField(max_length=20, verbose_name='学号')),
                ('spwd', models.CharField(max_length=20, verbose_name='密码')),
                ('shead', models.ImageField(upload_to='static/upload/shead', verbose_name='学生头像')),
                ('isActive', models.BooleanField(default=True, verbose_name='在读')),
            ],
            options={
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20, verbose_name='课程名称')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='学生成绩')),
            ],
            options={
                'verbose_name_plural': '学科',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20, verbose_name='教师姓名')),
                ('tphone', models.CharField(max_length=20, verbose_name='电话号码')),
                ('tpwd', models.CharField(max_length=20, verbose_name='密码')),
                ('temail', models.EmailField(max_length=254, verbose_name='电子邮件')),
                ('isActive', models.BooleanField(default=True, verbose_name='在职')),
                ('thead', models.ImageField(upload_to='static/upload/thead', verbose_name='教师头像')),
            ],
            options={
                'verbose_name_plural': '教师',
            },
        ),
    ]
