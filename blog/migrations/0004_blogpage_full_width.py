# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171016_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='full_width',
            field=models.BooleanField(default=False, verbose_name='Show this post as full-width (no sidebar)?'),
            preserve_default=False,
        ),
    ]