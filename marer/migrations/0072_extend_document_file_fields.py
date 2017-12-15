# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-15 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import marer.models.base
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0071_document_sign_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(max_length=512, upload_to=marer.models.base.documents_upload_path),
        ),
        migrations.AlterField(
            model_name='document',
            name='sign',
            field=models.FileField(blank=True, max_length=512, null=True, upload_to=marer.models.base.documents_upload_path),
        ),
    ]
