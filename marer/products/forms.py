from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ChoiceField, DateField, DecimalField, BooleanField, TextInput, DateInput, \
    IntegerField, HiddenInput, CheckboxInput, Select, NumberInput, Textarea, Field
from django.http import QueryDict
from djangoformsetjs.utils import formset_media_js

from marer.fields import BalanceCodeDecimalField
from marer import consts
from marer.models import BankMinimalCommission
from marer.products.fields import DecimalForcedThousandsGroupedField


class BGFinProdRegForm(Form):
    issuer_full_name = CharField(required=False)
    issuer_short_name = CharField(required=False)
    issuer_legal_address = CharField(required=False)

    issuer_ogrn = CharField(required=False)
    issuer_inn = CharField(required=False)
    issuer_kpp = CharField(required=False)

    tender_gos_number = CharField(required=False)
    tender_placement_type = CharField(required=False)
    tender_exec_law = ChoiceField(required=False, choices=[
        (consts.TENDER_EXEC_LAW_44_FZ, '44-ФЗ'),
        (consts.TENDER_EXEC_LAW_223_FZ, '223-ФЗ'),
        (consts.TENDER_EXEC_LAW_185_FZ, '185-ФЗ'),
        (consts.TENDER_EXEC_LAW_COMMERCIAL, 'Коммерческий'),
        (consts.TENDER_EXEC_LAW_CUSTOMS, 'Таможенная'),
        (consts.TENDER_EXEC_LAW_VAT, 'Возврат НДС'),
    ])
    tender_publish_date = DateField(required=False)
    tender_start_cost = DecimalField(decimal_places=2, required=False, localize=True)
    tender_final_cost = DecimalField(decimal_places=2, required=False, localize=True)

    tender_responsible_full_name = CharField(required=False)
    tender_responsible_legal_address = CharField(required=False)
    tender_responsible_inn = CharField(required=False)
    tender_responsible_kpp = CharField(required=False)
    tender_responsible_ogrn = CharField(required=False)

    bg_commercial_contract_subject = CharField(required=False)
    bg_commercial_contract_place_of_work = CharField(required=False)
    bg_commercial_contract_sum = DecimalField(decimal_places=2, required=False, localize=True)
    bg_commercial_contract_sign_date = DateField(required=False)
    bg_commercial_contract_end_date = DateField(required=False)

    balance_code_2400_offset_1 = BalanceCodeDecimalField(decimal_places=2, required=False, localize=True)
    balance_code_2400_offset_0 = BalanceCodeDecimalField(decimal_places=2, required=False, localize=True)

    bg_sum = DecimalForcedThousandsGroupedField(decimal_places=2, required=False, localize=True)
    bg_currency = ChoiceField(required=False, choices=[
        (consts.CURRENCY_RUR, 'Рубль'),
        (consts.CURRENCY_USD, 'Доллар'),
        (consts.CURRENCY_EUR, 'Евро'),
    ])
    bg_start_date = DateField(required=False)
    bg_end_date = DateField(required=False)
    bg_deadline_date = DateField(required=False)
    bg_type = ChoiceField(required=False, choices=[
        (consts.BG_TYPE_APPLICATION_ENSURE, 'Обеспечение заявки'),
        (consts.BG_TYPE_CONTRACT_EXECUTION, 'Исполнение контракта'),
        (consts.BG_TYPE_REFUND_OF_ADVANCE, 'Возврат аванса'),
        (consts.BG_TYPE_WARRANTY_ENSURE, 'Обеспечение гарантийных обязательств'),
    ])
    bg_is_benefeciary_form = BooleanField(required=False, widget=Select(attrs={'class': 'form-control'}, choices=[
        (True, 'Да'),
        (False, 'Нет'),
    ]))

    is_indisputable_charge_off = BooleanField(required=False,
                                              initial=True,
                                              widget=Select(
                                                  attrs={'class': 'form-control'}))

    tender_contract_type = ChoiceField(required=False, choices=[
        (consts.TENDER_CONTRACT_TYPE_SUPPLY_CONTRACT, 'Поставка товара'),
        (consts.TENDER_CONTRACT_TYPE_SERVICE_CONTRACT, 'Оказание услуг'),
        (consts.TENDER_CONTRACT_TYPE_WORKS_CONTRACT, 'Выполнение работ'),
    ])
    tender_contract_subject = CharField(widget=Textarea(), required=False)
    stop_factors = Field(required=False)
    tender_has_prepayment = BooleanField(required=False)
    already_has_an_agent = Field(required=False)

    def clean(self):
        bg_sum_min = BankMinimalCommission.objects.order_by('sum_min').first().sum_min
        bg_sum_max = BankMinimalCommission.objects.order_by('-sum_max').first().sum_max
        if not self.cleaned_data['bg_sum'] or not bg_sum_min < self.cleaned_data['bg_sum'] < bg_sum_max:
            self.add_error(None, 'Неверная сумма запрашиваемой гарантии')

        bg_start = self.cleaned_data['bg_start_date']
        bg_end = self.cleaned_data['bg_end_date']
        if bg_end and bg_start:
            bg_months_diff = 1 + (bg_end.year - bg_start.year) * 12 + bg_end.month - bg_start.month
        else:
            bg_months_diff = 0
        if not bg_start or not bg_end or not 0 < bg_months_diff < 30:
            self.add_error(None, 'Неверный срок действия запрашиваемой гарантии')

        balance_code_2400_offset_0 = self.cleaned_data['balance_code_2400_offset_0']
        balance_code_2400_offset_1 = self.cleaned_data['balance_code_2400_offset_1']
        if balance_code_2400_offset_0 < 0 or balance_code_2400_offset_1 < 0:
            self.add_error(None, 'Отрицательная прибыль')


class CreditFinProdRegForm(Form):
    credit_product_is_credit = BooleanField(required=False)
    credit_product_is_credit_line = BooleanField(required=False)
    credit_product_is_overdraft = BooleanField(required=False)

    credit_product_interest_rate = DecimalField(decimal_places=2, required=False, localize=True)
    credit_repayment_schedule = ChoiceField(required=False, choices=[
        (consts.ISSUE_CREDIT_REPAYMENT_SCHEDULE_EQUAL_SHARES, 'Равными долями'),
        (consts.ISSUE_CREDIT_REPAYMENT_SCHEDULE_END_OF_TERM, 'В конце срока'),
    ])
    credit_product_term = CharField(required=False)
    credit_product_cl_tranche_term = CharField(required=False)
    credit_purpose_type = ChoiceField(required=False, choices=[
        (consts.CREDIT_PURPOSE_TYPE_WORK_CAPITAL_REFILL, 'Пополнение оборотных средств'),
        (consts.CREDIT_PURPOSE_TYPE_CONTRACT_EXEC, 'Исполнение контракта'),
    ])
    credit_purpose = CharField(required=False)
    credit_repayment_sources = CharField(required=False)

    bg_sum = DecimalField(decimal_places=2, required=False, localize=True)
    bg_currency = ChoiceField(required=False, choices=[
        (consts.CURRENCY_RUR, 'Рубль'),
        (consts.CURRENCY_USD, 'Доллар'),
        (consts.CURRENCY_EUR, 'Евро'),
    ])

    issuer_full_name = CharField(required=False)
    issuer_short_name = CharField(required=False)
    issuer_legal_address = CharField(required=False)

    issuer_ogrn = CharField(required=False)
    issuer_inn = CharField(required=False)
    issuer_kpp = CharField(required=False)


class BGFinProdSurveyOrgCommonForm(Form):
    issuer_full_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_short_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_foreign_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_legal_address = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_fact_address = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Обязательно к заполнению'}))
    issuer_ogrn = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_inn = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_kpp = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_okpo = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_registration_date = DateField(required=False, widget=DateInput(attrs={'class': 'form-control'}))
    issuer_ifns_reg_date = DateField(required=False, widget=DateInput(attrs={'class': 'form-control'}))
    issuer_ifns_reg_cert_number = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_okopf = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_okved = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))

    avg_employees_cnt_for_prev_year = IntegerField(required=False, widget=NumberInput(attrs={'class': 'form-control'}))
    issuer_web_site = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_accountant_org_or_person = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Обязательно к заполнению'}))
    issuer_post_address = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_has_overdue_debts_for_last_180_days = BooleanField(required=False, widget=Select(attrs={'class': 'form-control'}, choices=[
        (False, 'Нет'),
        (True, 'Да'),
    ]))
    issuer_overdue_debts_info = CharField(required=False, widget=Textarea(attrs={'class': 'form-control', 'rows': 3}))
    tax_system = CharField(required=True, widget=Select(attrs={'class': 'form-control check'}, choices=[
        (None, '---Обязательно к выбору---'),
        (consts.TAX_USN, 'УСН'),
        (consts.TAX_OSN, 'ОСН'),
        (consts.TAX_ENVD, 'ЕНВД'),
        (consts.TAX_ESHD, 'ЕСХД'),
    ]))
    agent_comission = DecimalField(decimal_places=2, required=False,
                                   widget=TextInput(attrs={'class': 'form-control input-sm',
                                                           'placeholder': 'Предложить комиссию(руб)'}))


class BGFinProdSurveyOrgHeadForm(Form):
    issuer_head_first_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_last_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_middle_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_birthday = DateField(required=False, widget=DateInput(attrs={'class': 'form-control'}))
    issuer_head_org_position_and_permissions = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_phone = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_passport_series = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Обязательно к заполнению'}))
    issuer_head_passport_number = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Обязательно к заполнению'}))
    issuer_head_passport_issue_date = DateField(required=False, widget=DateInput(attrs={'class': 'form-control datepicker',
                                                                                        'placeholder': 'Обязательно к заполнению'}))
    issuer_head_passport_issued_by = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Обязательно к заполнению'}))
    issuer_head_residence_address = CharField(required=False, widget=TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Обязательно к заполнению'}))
    issuer_head_education_level = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_org_work_experience = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_share_in_authorized_capital = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_head_industry_work_experience = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_prev_org_info = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))

    def full_clean(self):
        if 'issuer_head_passport_issue_date' in self.data:
            try:
                fields = {k: v for k, v in self.fields.items()}
                fields.get('issuer_head_passport_issue_date').clean(self.data['issuer_head_passport_issue_date'])
            except ValidationError:
                new_qd = self.data.copy()
                del new_qd['issuer_head_passport_issue_date']
                self.data = QueryDict(new_qd.urlencode())

        return super().full_clean()


class BGFinProdSurveyOrgManagementForm(Form):
    issuer_org_management_collegial_executive_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_org_management_collegial_executive_fio = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_org_management_directors_or_supervisory_board_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_org_management_directors_or_supervisory_board_fio = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_org_management_other_name = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    issuer_org_management_other_fio = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))


class BGFinProdSurveyDealParamsForm(Form):
    bg_is_benefeciary_form = BooleanField(required=False, widget=Select(attrs={'class': 'form-control'}, choices=[
        (True, 'Да'),
        (False, 'Нет'),
    ]))
    is_indisputable_charge_off = BooleanField(required=False, widget=Select(attrs={'class': 'form-control'}, choices=[
        (True, 'Да'),
        (False, 'Нет'),
    ]))
    tender_contract_subject = CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    deal_has_beneficiary = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (True, 'Присутствует'),
        (False, 'Отсутствует'),
    ])
    issuer_bank_relations_term = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (consts.ISSUE_DEAL_BANK_RELATIONS_TERM_SHORT, 'Краткосрочные'),
        (consts.ISSUE_DEAL_BANK_RELATIONS_TERM_LONG, 'Долгосрочные'),
    ])
    issuer_activity_objective = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (consts.ISSUE_ISSUER_ACTIVITY_OBJECTIVE_PROFIT_MAKING, 'Получение прибыли'),
        (consts.ISSUE_ISSUER_ACTIVITY_OBJECTIVE_OTHER, 'Иное'),
    ])
    issuer_finance_situation = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (consts.ISSUE_ISSUER_FINANCE_SITUATION_SATISFIED, 'Удовлетворительное'),
        (consts.ISSUE_ISSUER_FINANCE_SITUATION_UNSATISFIED, 'Неудовлетворительное'),
    ])
    issuer_business_reputation = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (consts.ISSUE_ISSUER_BUSINESS_REPUTATION_POSITIVE, 'Положительная'),
        (consts.ISSUE_ISSUER_BUSINESS_REPUTATION_NOT_PRESENT, 'Отсутствует'),
    ])
    issuer_funds_source = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control'}), choices=[
        (consts.ISSUER_FUNDS_SOURCE_LOAN_FUNDS, 'Заемные средства'),
        (consts.ISSUER_FUNDS_SOURCE_OTHER, 'Иное'),
    ])


class AffiliatesForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    legal_address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    inn = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    activity_type = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    aff_percentage = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    aff_type = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class OrgBeneficiaryOwnerForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    legal_address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm req',
                                                                                      'placeholder': 'Обязательно к заполнению'}))
    fact_address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm req',
                                                                                      'placeholder': 'Обязательно к заполнению'}))
    post_address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    inn_or_snils = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    on_belong_to_pub_persons_info = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class OrgBankAccountForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    bik = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class FounderLegalForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    add_date = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    additional_business = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    country = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    auth_capital_percentage = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    legal_address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class FounderPhysicalForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    add_date = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    additional_business = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    country = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    auth_capital_percentage = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    address = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    passport_data = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class AgentComissionForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())

    class Media(object):
        js = formset_media_js


class OrgManagementCollegialForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    org_name = CharField(required=False, max_length=512,
                         widget=TextInput(attrs={'class': 'form-control input-sm',
                                                 'placeholder': 'Например, член совета директоров'}))
    fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class OrgManagementDirectorsForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    org_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm',
                                                                                 'placeholder': 'Например, член совета директоров'}))
    fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class OrgManagementOthersForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    org_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm',
                                                                                 'placeholder': 'Например, член совета директоров'}))
    fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class CreditPledgeForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())

    pledge_title = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    pledge_type = ChoiceField(required=False, widget=Select(attrs={'class': 'form-control input-sm'}), choices=[
        (consts.CREDIT_PLEDGE_TYPE_DEPOSIT, 'Депозит'),
        (consts.CREDIT_PLEDGE_TYPE_REAL_ESTATE, 'Недвижимость'),
        (consts.CREDIT_PLEDGE_TYPE_OTHER, 'Другое'),
    ])
    cost = DecimalField(decimal_places=2, required=False, localize=True, widget=TextInput(attrs={'class': 'form-control input-sm'}))

    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    def get_pledge_type_display(self):
        for val, val_name in self.fields['pledge_type'].choices:
            if val == self.initial.get('pledge_type', None):
                return val_name
        return ''

    class Media(object):
        js = formset_media_js


class LeasingFinProdRegForm(Form):
    leasing_term = IntegerField(required=False)
    leasing_advance_payment_rate = DecimalField(decimal_places=2, required=False, localize=True)
    leasing_payment_schedule = CharField(required=False)
    leasing_asset_operation_territory = CharField(required=False)
    leasing_bank_account_number = CharField(required=False)
    leasing_corr_account_number = CharField(required=False)
    leasing_bank_name = CharField(required=False)
    leasing_bank_identification_code = CharField(required=False)
    leasing_holder_on_balance_name = CharField(required=False)
    leasing_holder_on_balance_ogrn = CharField(required=False)
    leasing_holder_on_balance_inn = CharField(required=False)
    leasing_holder_on_balance_kpp = CharField(required=False)
    leasing_insurer_name = CharField(required=False)
    leasing_insurer_ogrn = CharField(required=False)
    leasing_insurer_inn = CharField(required=False)
    leasing_insurer_kpp = CharField(required=False)


class LeasingAssetForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    supplier_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    asset_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    asset_spec = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    asset_count = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    cost_with_vat = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    supply_term = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class LeasingSupplierForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    supplier_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    supplier_head_fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    supplier_contact_fio = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    supplier_contacts = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class LeasingPayRuleForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    asset_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    payment_name = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    payment_size = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    payment_rule = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js


class FactoringFinProdRegForm(Form):
    factoring_product_is_regressive = BooleanField(required=False)
    factoring_product_is_not_regressive = BooleanField(required=False)
    factoring_product_is_cred_risks_cover = BooleanField(required=False)
    factoring_product_is_suppliers_financing = BooleanField(required=False)
    factoring_product_is_orders_financing = BooleanField(required=False)
    factoring_product_is_closed = BooleanField(required=False)
    factoring_product_is_export = BooleanField(required=False)
    factoring_product_is_import = BooleanField(required=False)
    factoring_avg_actual_buyers_payment_term = IntegerField(required=False)
    factoring_max_contract_deferred_payment_term = IntegerField(required=False)
    factoring_sale_goods_or_services = CharField(required=False)
    factoring_manufactured_goods = CharField(required=False)


class FactoringSalesAnalyzeForm(Form):
    curr_year_sales_value = DecimalField(decimal_places=2, required=False, localize=True)
    prev_year_sales_value = DecimalField(decimal_places=2, required=False, localize=True)
    curr_year_sales_value_inc_deferment = DecimalField(decimal_places=2, required=False, localize=True)
    prev_year_sales_value_inc_deferment = DecimalField(decimal_places=2, required=False, localize=True)
    curr_year_expected_sales_value = DecimalField(decimal_places=2, required=False, localize=True)
    prev_year_expected_sales_value = DecimalField(decimal_places=2, required=False, localize=True)
    curr_year_expected_sales_value_inc_deferment = DecimalField(decimal_places=2, required=False, localize=True)
    prev_year_expected_sales_value_inc_deferment = DecimalField(decimal_places=2, required=False, localize=True)


class FactoringBuyerForm(Form):
    id = IntegerField(required=False, widget=HiddenInput())
    name_and_inn = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    avg_monthly_shipments = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    operating_pay_deferment_days = IntegerField(required=False, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    start_work_date = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    required_credit_limit = DecimalField(decimal_places=2, required=False, localize=True, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    debitor_share = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    average_delay_days = IntegerField(required=False, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    sales_volume = CharField(required=False, max_length=512, widget=TextInput(attrs={'class': 'form-control input-sm'}))
    DELETE = BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'hidden'}))

    class Media(object):
        js = formset_media_js
