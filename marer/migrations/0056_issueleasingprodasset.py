# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0055_nullable_issuedocument_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueLeasingProdAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(default='', max_length=512, verbose_name='наименование поставщика/продавца')),
                ('asset_name', models.CharField(default='', max_length=512, verbose_name='наименование, тип, модель')),
                ('asset_spec', models.CharField(default='', max_length=512, verbose_name='спецификация')),
                ('asset_count', models.CharField(default='', max_length=512, verbose_name='количество')),
                ('cost_with_vat', models.CharField(default='', max_length=512, verbose_name='стоимость с НДС')),
                ('supply_term', models.CharField(default='', max_length=512, verbose_name='срок поставки')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leasing_assets', to='marer.Issue')),
            ],
            options={
                'verbose_name': 'лизинговое имущество',
                'verbose_name_plural': 'лизинговое имущество',
            },
        ),
    ]