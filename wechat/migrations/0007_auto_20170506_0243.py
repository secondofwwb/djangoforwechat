# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-06 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_auto_20170501_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icons',
            old_name='labeid',
            new_name='labelid',
        ),
    ]
