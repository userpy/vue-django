# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0015_fill_issue_model_with_bg_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueFinanceOrgProposeClarification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.CharField(choices=[('finance_org', 'Финансовая организация'), ('issuer', 'Заявитель')], max_length=32)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('propose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clarifications', to='marer.IssueFinanceOrgPropose')),
            ],
        ),
    ]
