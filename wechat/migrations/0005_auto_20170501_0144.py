# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0004_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='recimfor',
            field=models.CharField(choices=[('REC', 'REC'), ('NOREC', 'NOREC')], default='NOREC', max_length=10),
        ),
    ]
