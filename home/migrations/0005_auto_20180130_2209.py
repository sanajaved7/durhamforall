# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171203_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='search_description_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='search_description_es',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='seo_title_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='seo_title_es',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slug_es',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='url_path_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='url_path_es',
        ),
    ]