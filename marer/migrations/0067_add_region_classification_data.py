# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-06 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0066_add_issue_finance_balance_related_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionKLADRCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='region',
            name='okato_code',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='region',
            name='oktmo_code',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='regionkladrcode',
            name='region',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kladr_codes', to='marer.Region'),
        ),
    ]
