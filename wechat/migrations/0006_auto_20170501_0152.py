# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0005_auto_20170501_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_image',
            field=models.ImageField(blank=True, null=True, upload_to='contentimage/'),
        ),
    ]
