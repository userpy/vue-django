# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-22 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0119_enlarge_issue_tender_placement_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='tender_contract_subject',
            field=models.CharField(blank=True, default='', max_length=8192, verbose_name='предмет контракта'),
        ),
    ]
