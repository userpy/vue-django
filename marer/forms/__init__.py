from django.forms import Form, DecimalField, DateField, BooleanField, ChoiceField
from django.forms import fields
from django.forms.widgets import TextInput, PasswordInput, EmailInput, Select, Textarea, HiddenInput

from marer import consts
from marer.forms.widgets import CallableChoicesSelect
from marer.models.user import User
from marer.products import get_finance_products_as_choices


class RegisterForm(Form):
    first_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Имя'
    )
    last_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Фамилия'
    )
    email = fields.EmailField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
    phone = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Контактный телефон'
    )
    password = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )
    password_repeat = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль еще раз'
    )

    def is_valid(self):
        if self.data['password'] != self.data['password_repeat']:
            self.add_error(None, 'Введенные пароли не совпадают')
        return super().is_valid()


class LoginForm(Form):
    email = fields.EmailField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
    password = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )


class LoginSignForm(Form):
    cert = fields.CharField(
        required=True,
        widget=Select(attrs={'class': 'form-control'}),
        label='Сертификат'
    )
    signature = fields.CharField(
        required=True,
        widget=HiddenInput
    )


class RegisterSignForm(Form):
    first_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Имя'
    )
    last_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Фамилия'
    )
    email = fields.EmailField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
    phone = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Контактный телефон'
    )
    cert = fields.CharField(
        required=True,
        widget=HiddenInput
    )
    signature = fields.CharField(
        required=True,
        widget=HiddenInput
    )


class ProfileForm(Form):
    first_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Имя'
    )
    last_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Фамилия'
    )
    phone = fields.CharField(
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Контактный телефон'
    )


class ChangePasswordForm(Form):
    user = None

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    old_password = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Старый пароль'
    )
    password = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Новый пароль'
    )
    password_repeat = fields.CharField(
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль еще раз'
    )

    def _get_field_data(self, field_name):
        if self.prefix:
            return self.data[self.prefix + '-' + field_name]
        else:
            return self.data[field_name]

    def is_valid(self):
        if not self.user.check_password(self._get_field_data('old_password')):
            self.add_error('old_password', 'Указан неверный старый пароль')
        if self._get_field_data('password') != self._get_field_data('password_repeat'):
            self.add_error(None, 'Введенные пароли не совпадают')
        return super().is_valid()


class QuickRequestForm(Form):

    product = fields.CharField(
        required=True,
        widget=Select(
            choices=get_finance_products_as_choices(),
            attrs={'class': 'orderinputtop w-input'}
        ),
        label='Вид услуги'
    )

    party = fields.CharField(
        required=True,
        widget=TextInput(attrs={
            'class': 'orderinputtop w-input party',
            'placeholder': 'Название, ИНН, ОГРН или адрес организации',
        }),
        label='Организация'
    )

    party_ogrn = fields.CharField(required=False, widget=HiddenInput())
    party_inn = fields.CharField(required=False, widget=HiddenInput())
    party_kpp = fields.CharField(required=False, widget=HiddenInput())
    party_okved = fields.CharField(required=False, widget=HiddenInput())
    party_okopf = fields.CharField(required=False, widget=HiddenInput())

    party_full_name = fields.CharField(required=False, widget=HiddenInput())
    party_short_name = fields.CharField(required=False, widget=HiddenInput())
    party_foreign_name = fields.CharField(required=False, widget=HiddenInput())
    party_legal_address = fields.CharField(required=False, widget=HiddenInput())

    party_head_fio = fields.CharField(required=False, widget=HiddenInput())
    party_head_position = fields.CharField(required=False, widget=HiddenInput())

    contact_person_name = fields.CharField(
        required=True,
        widget=TextInput(attrs={
            'class': 'orderinputtop w-input',
            'placeholder': 'Контактное лицо',
        }),
        label='Контактное лицо'
    )
    contact_phone = fields.CharField(
        required=True,
        widget=TextInput(attrs={
            'class': 'orderinputtop w-input',
            'placeholder': 'Номер телефона',
        }),
        label='Телефон'
    )
    contact_email = fields.EmailField(
        required=True,
        widget=TextInput(attrs={
            'class': 'orderinputtop w-input',
            'placeholder': 'Электронная почта',
        }),
        label='E-mail'
    )

    def __init__(self, *args, user: User = None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.initial.update(dict(
                contact_person_name=user.get_full_name(),
                contact_email=user.email,
                contact_phone=user.phone,
            ))
            self.fields['contact_person_name'].disabled = True
            self.fields['contact_email'].disabled = True
            self.fields['contact_phone'].disabled = True


class CabinetIssueListFilterForm(Form):
    fpgrp = fields.CharField(
        required=False,
        widget=Select(
            choices=get_finance_products_as_choices(),
            attrs={'class': 'form-control', 'style': 'max-width: 300px;'}
        ),
        label='Вид заявки'
    )
    status = fields.CharField(
        required=False,
        widget=CallableChoicesSelect(
            choices=[
                (None, 'Все'),
                (consts.ISSUE_STATUS_REGISTERING, 'Оформление заявки'),
                (consts.ISSUE_STATUS_REVIEW, 'Рассмотрение заявки'),
                (consts.ISSUE_STATUS_FINISHED, 'Завершена'),
                (consts.ISSUE_STATUS_CANCELLED, 'Отменена'),
                # (consts.ISSUE_STATUS_CLIENT_REVISION, 'Отправлено клиенту на доработку'),
                # (consts.ISSUE_STATUS_RETURNED_FROM_REVISION, 'Возвращена с доработки'),
                # (consts.ISSUE_STATUS_CLIENT_AGGREEMENT, 'Отправлено на согласование клиенту'),
                # (consts.ISSUE_STATUS_CANCELLED_BY_CLIENT, 'Отменена клиентом'),
            ],
            attrs={'class': 'form-control'}
        ),
        label='Статус заявки'
    )


class IssueRegisteringForm(Form):
    product = fields.CharField(
        required=True,
        widget=Select(
            choices=get_finance_products_as_choices(),
            attrs={'class': 'form-control'}
        ),
        label='Вид заявки',
    )
    org_search_name = fields.CharField(
        required=False,
        widget=TextInput(attrs={'class': 'form-control'}),
        label='Организация',
    )
    comment = fields.CharField(
        required=False,
        widget=Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Комментарий к заявке',
    )
    issuer_full_name = fields.CharField(required=False)
    issuer_short_name = fields.CharField(required=False)
    issuer_legal_address = fields.CharField(required=False)

    issuer_ogrn = fields.CharField(required=False)
    issuer_inn = fields.CharField(required=False)
    issuer_kpp = fields.CharField(required=False)


class RestTenderForm(Form):
    gos_number = fields.CharField(required=True, max_length=512)


class IssueBankCommissionForm(Form):
    bg_sum = DecimalField(decimal_places=2, required=True, localize=True)
    bg_start_date = DateField(required=True)
    bg_end_date = DateField(required=True)
    bg_is_benefeciary_form = BooleanField(required=False, widget=Select(attrs={'class': 'form-control'}, choices=[
        (True, 'Да'),
        (False, 'Нет'),
    ]))
    tender_has_prepayment = BooleanField(required=False)
    bg_type = ChoiceField(required=True, choices=[
        (consts.BG_TYPE_CONTRACT_EXECUTION, 'Исполнение контракта'),
        (consts.BG_TYPE_APPLICATION_ENSURE, 'Обеспечение заявки на участие в тендере'),
        (consts.BG_TYPE_REFUND_OF_ADVANCE, 'Возврат аванса'),
        (consts.BG_TYPE_WARRANTY_ENSURE, 'Обеспечение гарантийных обязательств')
    ])
    tender_exec_law = ChoiceField(required=True, choices=[
        (consts.TENDER_EXEC_LAW_44_FZ, '44-ФЗ'),
        (consts.TENDER_EXEC_LAW_223_FZ, '223-ФЗ'),
        (consts.TENDER_EXEC_LAW_185_FZ, '185-ФЗ'),
        (consts.TENDER_EXEC_LAW_COMMERCIAL, 'Коммерческий'),
        (consts.TENDER_EXEC_LAW_CUSTOMS, 'Таможенная'),
        (consts.TENDER_EXEC_LAW_VAT, 'Возврат НДС'),
    ])


class IFOPCMessageForm(Form):
    message = fields.CharField(
        required=True,
        widget=Textarea(attrs={'class': 'form-control', 'rows': 4}),
    )
    doc1 = fields.FileField(required=False)
    doc2 = fields.FileField(required=False)
    doc3 = fields.FileField(required=False)
    doc4 = fields.FileField(required=False)
    doc5 = fields.FileField(required=False)
    doc6 = fields.FileField(required=False)
    doc7 = fields.FileField(required=False)
    doc8 = fields.FileField(required=False)


class EmailForm(Form):
    email = fields.EmailField(required=False,
                              widget=TextInput(attrs={'class': 'form-control send-to-client',
                                                      'id': 'email',
                                                      'placeholder': 'Введите email клиента'}))
