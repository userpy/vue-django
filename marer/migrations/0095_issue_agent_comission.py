# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-08 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0094_add_contract_guarantee'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='agent_comission',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Комиссия агента'),
        ),
    ]