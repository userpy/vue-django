# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0028_region_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='private_comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
