# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 01:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_icons_icon_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='icons',
        ),
    ]