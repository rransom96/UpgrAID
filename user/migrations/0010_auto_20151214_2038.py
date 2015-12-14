# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0009_achievement_required_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='user',
        ),
        migrations.AddField(
            model_name='earned',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Achievement'),
        ),
        migrations.AddField(
            model_name='earned',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='achievement',
            name='user',
            field=models.ManyToManyField(related_name='achievement_set', through='user.Earned', to=settings.AUTH_USER_MODEL),
        ),
    ]