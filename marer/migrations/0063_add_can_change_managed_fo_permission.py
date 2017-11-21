# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0062_extend_issue_tender_gos_number_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financeorganization',
            options={'permissions': [('can_change_managed_finance_orgs', 'Can change managed finance orgs'), ('can_change_managed_finance_org_proposes', 'Can change managed finance org proposes'), ('can_view_managed_finance_org_proposes_issues', 'Can view managed finance org proposes issues'), ('can_add_managed_finance_org_proposes_clarifications', 'Can add managed finance org proposes clarifications'), ('can_view_managed_finance_org_proposes_clarifications', 'Can view managed finance org proposes clarifications'), ('can_add_managed_finance_org_proposes_clarifications_messages', 'Can add managed finance org proposes clarifications messages')], 'verbose_name': 'финансовая орнанизация', 'verbose_name_plural': 'финансовые организации'},
        ),
    ]