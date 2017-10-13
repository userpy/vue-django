# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0031_user_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeorganization',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='менеджер'),
        ),
    ]