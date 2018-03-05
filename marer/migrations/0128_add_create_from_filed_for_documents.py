# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def set_created_from_values(apps, schema_editor):
    FinanceOrgProductProposeDocument = apps.get_model('marer', 'FinanceOrgProductProposeDocument')
    IssueProposeDocument = apps.get_model('marer', 'IssueProposeDocument')
    for fdoc in FinanceOrgProductProposeDocument.objects.all():
        IssueProposeDocument.objects.filter(name=fdoc.name).update(created_from_id=fdoc.id)


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0127_shorten_issue_db_columns_names_longer_63_symbols'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueproposedocument',
            name='created_from',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='marer.FinanceOrgProductProposeDocument', blank=True, null=True),
            preserve_default=False,

        ),
        migrations.RunPython(set_created_from_values, migrations.RunPython.noop)
    ]
