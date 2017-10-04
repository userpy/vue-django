# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0018_issuefinanceorgproposeclarificationmessagedocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBGProdAffiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512)),
                ('legal_address', models.CharField(default='', max_length=512)),
                ('inn', models.CharField(default='', max_length=512)),
                ('activity_type', models.CharField(default='', max_length=512)),
                ('aff_percentage', models.CharField(default='', max_length=512)),
                ('aff_type', models.CharField(default='', max_length=512)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuer_affiliates', to='marer.Issue')),
            ],
        ),
    ]