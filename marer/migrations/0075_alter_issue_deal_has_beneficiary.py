# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0074_add_xlsx_form_issue_related_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='deal_has_beneficiary',
            field=models.NullBooleanField(verbose_name='наличие бенефициара по сделке'),
        ),
    ]