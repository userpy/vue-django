# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0054_add_issue_leasing_related_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedocument',
            name='code',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
