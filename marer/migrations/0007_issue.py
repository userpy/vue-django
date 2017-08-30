# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0006_financeproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('BankGuaranteeProduct', 'Банковская гарантия'), ('CreditProduct', 'Кредит'), ('LeasingProduct', 'Лизинг')], max_length=32)),
                ('status', models.CharField(choices=[('registering', 'Оформление заявки'), ('common_documents_request', 'Запрос документов'), ('survey', 'Анкетирование'), ('scoring', 'Скоринг'), ('additional_documents_request', 'Дозапрос документов'), ('payments', 'Оплата услуг'), ('final_documents_approval', 'Согласование итоговых документов'), ('finished', 'Завершена'), ('cancelled', 'Отменена')], max_length=32)),
                ('sum', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('comment', models.TextField(default='')),
                ('issuer_inn', models.CharField(max_length=32)),
                ('issuer_kpp', models.CharField(max_length=32)),
                ('issuer_ogrn', models.CharField(max_length=32)),
                ('issuer_full_name', models.CharField(max_length=512)),
                ('issuer_short_name', models.CharField(max_length=512)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
