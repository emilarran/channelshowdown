# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestream', '0002_remove_episode_archive_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='archive_id',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
