# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-28 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0124_make_issue_agent_commission_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_ordinary_manager',
            field=models.BooleanField(default=False, verbose_name='Пользователь является менеджером и видит только свои заявки'),
        ),
    ]
