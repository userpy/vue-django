# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


def fill_finance_products(apps, schema_editor):
    finance_product_model = apps.get_model("marer", "FinanceProduct")
    finance_product_model(id=1, name='Госконтракты', parent_id=None, lft=1, rght=12, tree_id=1, level=0).save()
    finance_product_model(id=7, name='Тендерный кредит', parent_id=1, lft=2, rght=3, tree_id=1, level=1).save()
    finance_product_model(id=8, name='БГ на обеспечение заявки', parent_id=1, lft=4, rght=5, tree_id=1, level=1).save()
    finance_product_model(id=9, name='БГ на обеспечение контракта', parent_id=1, lft=6, rght=7, tree_id=1, level=1).save()
    finance_product_model(id=10, name='Кредит на исполнение госконтракта', parent_id=1, lft=8, rght=9, tree_id=1, level=1).save()
    finance_product_model(id=11, name='БГ на возврат аванса', parent_id=1, lft=10, rght=11, tree_id=1, level=1).save()
    finance_product_model(id=2, name='Кредитные организации', parent_id=None, lft=1, rght=24, tree_id=2, level=0).save()
    finance_product_model(id=12, name='Овердрафт', parent_id=2, lft=2, rght=3, tree_id=2, level=1).save()
    finance_product_model(id=13, name='Возобновляемая кредитная линия', parent_id=2, lft=4, rght=5, tree_id=2, level=1).save()
    finance_product_model(id=14, name='Невозобновляемая кредитная линия', parent_id=2, lft=6, rght=7, tree_id=2, level=1).save()
    finance_product_model(id=15, name='Кредитное исполнение контракта', parent_id=2, lft=8, rght=9, tree_id=2, level=1).save()
    finance_product_model(id=16, name='Кредит на пополнение оборотных средств', parent_id=2, lft=10, rght=11, tree_id=2, level=1).save()
    finance_product_model(id=17, name='Мезонинное кредитование', parent_id=2, lft=12, rght=13, tree_id=2, level=1).save()
    finance_product_model(id=18, name='Синдицированное кредитование', parent_id=2, lft=14, rght=15, tree_id=2, level=1).save()
    finance_product_model(id=19, name='Проектное финансирвоание', parent_id=2, lft=16, rght=17, tree_id=2, level=1).save()
    finance_product_model(id=20, name='Рассчетно-кассовое обслуживание', parent_id=2, lft=18, rght=19, tree_id=2, level=1).save()
    finance_product_model(id=21, name='Зарплатные проекты', parent_id=2, lft=20, rght=21, tree_id=2, level=1).save()
    finance_product_model(id=22, name='Внешняя экономическая деятельность', parent_id=2, lft=22, rght=23, tree_id=2, level=1).save()
    finance_product_model(id=3, name='Лизинг', parent_id=None, lft=1, rght=8, tree_id=3, level=0).save()
    finance_product_model(id=23, name='Лизинг автотранспорта', parent_id=3, lft=2, rght=3, tree_id=3, level=1).save()
    finance_product_model(id=24, name='Лизинг оборудования', parent_id=3, lft=4, rght=5, tree_id=3, level=1).save()
    finance_product_model(id=25, name='Лизинг спецтехники', parent_id=3, lft=6, rght=7, tree_id=3, level=1).save()
    finance_product_model(id=4, name='Факторинг', parent_id=None, lft=1, rght=14, tree_id=4, level=0).save()
    finance_product_model(id=26, name='Классический факторинг', parent_id=4, lft=2, rght=3, tree_id=4, level=1).save()
    finance_product_model(id=27, name='Конфиденциальный факторинг', parent_id=4, lft=4, rght=5, tree_id=4, level=1).save()
    finance_product_model(id=28, name='Бездокументарный факторинг', parent_id=4, lft=6, rght=7, tree_id=4, level=1).save()
    finance_product_model(id=29, name='Безрегрессный факторинг', parent_id=4, lft=8, rght=9, tree_id=4, level=1).save()
    finance_product_model(id=30, name='Реверсивный факторинг', parent_id=4, lft=10, rght=11, tree_id=4, level=1).save()
    finance_product_model(id=31, name='Дополнительная отсрочка платежа дебитору', parent_id=4, lft=12, rght=13, tree_id=4, level=1).save()
    finance_product_model(id=5, name='Страхование', parent_id=None, lft=1, rght=14, tree_id=5, level=0).save()
    finance_product_model(id=32, name='Автокредитование', parent_id=5, lft=2, rght=3, tree_id=5, level=1).save()
    finance_product_model(id=33, name='Добровольное медицинское страхование', parent_id=5, lft=4, rght=5, tree_id=5, level=1).save()
    finance_product_model(id=34, name='Строймонтажные риски', parent_id=5, lft=6, rght=7, tree_id=5, level=1).save()
    finance_product_model(id=35, name='Страхование гражданской ответственности застройщика (214-ФЗ)', parent_id=5, lft=8, rght=9, tree_id=5, level=1).save()
    finance_product_model(id=36, name='Страхование грузов', parent_id=5, lft=10, rght=11, tree_id=5, level=1).save()
    finance_product_model(id=37, name='Страхование жизни', parent_id=5, lft=12, rght=13, tree_id=5, level=1).save()
    finance_product_model(id=6, name='Инвестиции', parent_id=None, lft=1, rght=6, tree_id=6, level=0).save()
    finance_product_model(id=38, name='Венчурные фонды', parent_id=6, lft=2, rght=3, tree_id=6, level=1).save()
    finance_product_model(id=39, name='Частные инвесторы', parent_id=6, lft=4, rght=5, tree_id=6, level=1).save()


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0006_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('_seo_h1', models.CharField(blank=True, default='', max_length=512)),
                ('_seo_title', models.CharField(blank=True, default='', max_length=512)),
                ('_seo_description', models.CharField(blank=True, default='', max_length=512)),
                ('_seo_keywords', models.CharField(blank=True, default='', max_length=512)),
                ('page_content', models.TextField(blank=True, default='')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='marer.FinanceProduct')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(fill_finance_products, migrations.RunPython.noop)
    ]
