from django.forms import Form
from django.forms import fields
from django.forms import widgets


class RegisterForm(Form):
    first_name = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Имя'
    )
    last_name = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Фамилия'
    )
    email = fields.EmailField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
    phone = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Контактный телефон'
    )
    password = fields.CharField(
        required=True,
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )
    password_repeat = fields.CharField(
        required=True,
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль еще раз'
    )

    def is_valid(self):
        if self.data['password'] != self.data['password_repeat']:
            self.add_error(None, 'Введенные пароли не совпадают')
        return super().is_valid()


class LoginForm(Form):
    email = fields.EmailField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
    password = fields.CharField(
        required=True,
        widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль'
    )


class ProfileForm(Form):
    first_name = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Имя'
    )
    last_name = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Фамилия'
    )
    phone = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Контактный телефон'
    )


class QuickRequestForm(Form):

    finance_product = fields.CharField(
        required=True,
        widget=widgets.Select(
            choices=[],
            attrs={'class': 'form-control'}
        ),
        label='Вид услуги'
    )
    issuer = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Название или ИНН органиазции'
    )
    contact_person_name = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Контактное лицо'
    )
    contact_phone = fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
        label='Телефон'
    )
    contact_email = fields.EmailField(
        required=True,
        widget=widgets.EmailInput(attrs={'class': 'form-control'}),
        label='E-mail'
    )
