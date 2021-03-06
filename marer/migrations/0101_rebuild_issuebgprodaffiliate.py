# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-09 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0100_issue_is_contract_corresponds_issuer_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebgprodaffiliate',
            name='activity_type',
        ),
        migrations.RemoveField(
            model_name='issuebgprodaffiliate',
            name='aff_percentage',
        ),
        migrations.RemoveField(
            model_name='issuebgprodaffiliate',
            name='legal_address',
        ),
        migrations.RemoveField(
            model_name='issuebgprodaffiliate',
            name='aff_type',
        ),
        migrations.AddField(
            model_name='issuebgprodaffiliate',
            name='bank_liabilities_vol',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='объем обязательств банка'),
        ),
    ]
