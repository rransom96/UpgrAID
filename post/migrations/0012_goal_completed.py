# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_remove_post_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]