# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20151215_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='goal',
        ),
    ]