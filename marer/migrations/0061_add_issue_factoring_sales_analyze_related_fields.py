# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marer', '0060_issuefactoringbuyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='curr_year_expected_sales_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Ожидаемые продажи за текущий год по экспорту, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='curr_year_expected_sales_value_inc_deferment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Ожидаемые продажи за текущий год по экспорту в том числе с отсрочкой платежа, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='curr_year_sales_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Объем продаж за текущий год, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='curr_year_sales_value_inc_deferment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Объем продаж за текущий год, в том числе на условиях отсрочки, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='prev_year_expected_sales_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Ожидаемые продажи за прошлый год по экспорту, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='prev_year_expected_sales_value_inc_deferment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Ожидаемые продажи за прошлый год по экспорту в том числе с отсрочкой платежа, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='prev_year_sales_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Объем продаж за прошлый год, млн. рублей без НДС'),
        ),
        migrations.AddField(
            model_name='issue',
            name='prev_year_sales_value_inc_deferment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Объем продаж за прошлый год, в том числе на условиях отсрочки, млн. рублей без НДС'),
        ),
    ]
