# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icons',
            name='icon_image',
            field=models.ImageField(null=True, upload_to='iconimage/'),
        ),
    ]