# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20151215_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Rank'),
        ),
    ]
