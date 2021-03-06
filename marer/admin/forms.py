from django import forms
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField, UsernameField
from django.forms import Select
from django.utils.translation import ugettext_lazy as _

from marer import consts, models
from marer.forms.widgets import ReadOnlyFileInput
from marer.models import IssueClarificationMessage, Document, \
    IssueFinanceOrgProposeClarificationMessageDocument
from marer.models.finance_org import FinanceOrgProductProposeDocument
from marer.utils.notify import notify_managers_about_new_message_in_chat


class IFOPClarificationAddForm(forms.ModelForm):
    user = None
    message = forms.CharField(label='Сообщение', required=True, widget=forms.Textarea(attrs=dict(rows=4)))
    doc1 = forms.FileField(label='Документ', required=False)
    doc2 = forms.FileField(label='Документ', required=False)
    doc3 = forms.FileField(label='Документ', required=False)
    doc4 = forms.FileField(label='Документ', required=False)
    doc5 = forms.FileField(label='Документ', required=False)
    doc6 = forms.FileField(label='Документ', required=False)
    doc7 = forms.FileField(label='Документ', required=False)
    doc8 = forms.FileField(label='Документ', required=False)

    def save(self, commit=True):
        change = True
        if not self.instance.id:
            self.instance.initiator = consts.IFOPC_INITIATOR_FINANCE_ORG
            self.instance.save()
            change = False

        new_msg = IssueClarificationMessage()
        new_msg.user = self.user
        new_msg.message = self.cleaned_data['message']
        new_msg.issue = self.instance
        new_msg.save()

        for file_field_name in self.files:
            field_file = self.files[file_field_name]

            new_ifopcmd_doc = Document()
            new_ifopcmd_doc.file = field_file
            new_ifopcmd_doc.save()

            new_ifopcmd = IssueFinanceOrgProposeClarificationMessageDocument()
            new_ifopcmd.name = field_file.name
            new_ifopcmd.clarification_message = new_msg
            new_ifopcmd.document = new_ifopcmd_doc
            new_ifopcmd.save()

        notify_managers_about_new_message_in_chat(new_msg)
        return super().save(commit)


class MarerUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            'Пароли хранятся в защищённом виде, так что у нас нет способа '
            'узнать пароль этого пользователя. Однако вы можете сменить '
            'его/её пароль, используя <a href="../password/">эту форму</a>.'
            '<br/>Или же вы можете сбросить пароль пользователя на '
            'сгенерированный автоматически и выслать новые данные для входа '
            'письмом, используя <a href="../password/reset/">эту форму</a>.'
        ),
    )


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ()
        field_classes = {'email': UsernameField}

    def __init__(self, *args, **kwargs):
        if 'email' in self.base_fields:
            self.base_fields['email'].help_text = 'Если не заполнено, используется имя пользователя.'
        super(UserCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        if 'email' in self.cleaned_data and 'username' in self.cleaned_data:
            if self.cleaned_data['email'] == '':
                self.cleaned_data['email'] = self.cleaned_data['username']

        return super().clean()


class FinanceOrgProductProposeDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=False, label='Образец', widget=ReadOnlyFileInput)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.sample:
                initial['file'] = instance.sample.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if 'file' in self.cleaned_data:
            new_doc = Document()
            new_doc.file = self.cleaned_data['file']
            new_doc.save()
            self.instance.sample = new_doc
        return super().save(commit)


class IFOPFinalDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=True, label='файл', widget=ReadOnlyFileInput)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.document:
                initial['file'] = instance.document.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        new_doc = Document()
        new_doc.file = self.cleaned_data['file']
        new_doc.save()
        self.instance.document = new_doc
        return super().save(commit)


class IFOPFormalizeDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=True, label='файл', widget=ReadOnlyFileInput)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.document:
                initial['file'] = instance.document.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        new_doc = Document()
        new_doc.file = self.cleaned_data['file']
        new_doc.save()
        self.instance.document = new_doc
        return super().save(commit)


class IssueDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=True, label='файл', widget=ReadOnlyFileInput)
    code = forms.CharField(required=False, widget=Select(choices=[]))
    issue = None

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.document:
                initial['file'] = instance.document.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        new_doc = Document()
        new_doc.file = self.cleaned_data['file']
        new_doc.save()
        self.instance.document = new_doc
        return super().save(commit)


class IssueProposeDocumentInlineAdminForm(forms.ModelForm):
    file_sample = forms.FileField(required=False, label='образец')
    file = forms.FileField(required=False, label='файл')

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.sample:
                initial['file_sample'] = instance.sample.file
            if instance.document and instance.document.file and instance.document.file != 'False':
                initial['file'] = instance.document.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if 'file' in self.cleaned_data:
            new_doc = Document()
            new_doc.file = self.cleaned_data['file']
            new_doc.save()
            self.instance.document = new_doc
        if 'file_sample' in self.cleaned_data:
            new_sample = Document()
            new_sample.file = self.cleaned_data['file_sample']
            new_sample.save()
            self.instance.sample = new_sample
        return super().save(commit)


class FinanceOrgProductProposeDocumentForm(forms.ModelForm):

    class Meta:
        model = FinanceOrgProductProposeDocument
        fields = (
            'finance_product',
            'name',
            'file_sample',
            'code',
            'type',
            'tax_system',
            'form_ownership',
            'min_bg_sum',
            'max_bg_sum',
            'is_required',
            'if_not_finished_contracts',
        )

    file_sample = forms.FileField(label='Образец', required=False)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        if instance is not None:
            initial = kwargs.get('initial', dict())
            if instance.sample:
                initial['file_sample'] = instance.sample.file
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if 'file_sample' in self.cleaned_data:
            if self.cleaned_data['file_sample']:
                new_sample = Document()
                new_sample.file = self.cleaned_data['file_sample']
                new_sample.save()
                self.instance.sample = new_sample
            else:
                self.instance.sample = None
            # self.cleaned_data['sample'] = new_sample
        return super().save(commit)
