# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0029_issue_private_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedocument',
            name='code',
            field=models.CharField(max_length=512),
        ),
    ]