# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0086_issueorgmanagementcollegial_issueorgmanagementdirectors_issueorgmanagementothers'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueMessagesProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('marer.issue',),
        ),
    ]
