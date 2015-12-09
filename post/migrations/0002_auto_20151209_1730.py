# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 17:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 17, 30, 13, 5534, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 17, 30, 19, 915399, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 17, 30, 26, 325893, tzinfo=utc)),
            preserve_default=False,
        ),
    ]