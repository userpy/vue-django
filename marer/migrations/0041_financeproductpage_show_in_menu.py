# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0040_newspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeproductpage',
            name='show_in_menu',
            field=models.BooleanField(default=True, verbose_name='show in menu'),
        ),
    ]