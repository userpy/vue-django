# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0042_add_credit_related_fields_to_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueCreditPledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pledge_title', models.CharField(default='', max_length=512, verbose_name='наименование')),
                ('pledge_type', models.CharField(choices=[('deposit', 'Депозит'), ('real_estate', 'Недвижимость'), ('other', 'Другое')], max_length=32, verbose_name='вид')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='сумма')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuer_credit_pledges', to='marer.Issue')),
            ],
        ),
    ]
