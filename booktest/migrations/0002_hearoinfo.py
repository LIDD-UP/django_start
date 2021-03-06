# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-31 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HearoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, verbose_name='英雄姓名')),
                ('hsex', models.IntegerField(blank=True, choices=[('0', '男'), ('1', '女'), ('2', '秘密')], default=2, verbose_name='性别')),
                ('hcomment', models.CharField(max_length=200, verbose_name='英雄评论')),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]
