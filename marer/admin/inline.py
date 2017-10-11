from django.contrib.admin import StackedInline, TabularInline
from django import forms
from django.db.models import TextField
from django.forms import Select

from marer import models
from marer.forms.widgets import ReadOnlyFileInput
from marer.models import Document
from marer.models.issue import IssueFinanceOrgProposeFormalizeDocument, IssueFinanceOrgProposeFinalDocument, \
    IssueBGProdAffiliate, IssueBGProdFounderLegal, IssueBGProdFounderPhysical


class IssueFinanceOrgProposeInlineAdmin(StackedInline):
    extra = 1
    model = models.IssueFinanceOrgPropose
    fields = ('finance_org',)
    show_change_link = True


class IssueDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=True, label='файл', widget=ReadOnlyFileInput)
    code = forms.CharField(required=True, widget=Select(choices=[]))
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


class IssueDocumentInlineAdmin(TabularInline):
    extra = 0
    fields = (
        'code',
        'file',
    )
    model = models.IssueDocument
    form = IssueDocumentInlineAdminForm

    def get_formset(self, request, obj=None, **kwargs):
        choices = [(ch.code, ch.name) for ch in obj.get_product().get_documents_list()]
        self.form.declared_fields['code'].widget.choices = choices
        return super().get_formset(request, obj, **kwargs)


class IFOPClarificationInlineAdmin(TabularInline):
    model = models.IssueFinanceOrgProposeClarification
    show_change_link = True
    fields = (
        'humanized_id',
        'issue_str',
        'propose_finance_org',
        'initiator',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'humanized_id',
        'issue_str',
        'propose_finance_org',
        'initiator',
        'created_at',
        'updated_at',
    )
    classes = ('collapse',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def propose_finance_org(self, obj):
        return obj.propose.finance_org.name
    propose_finance_org.short_description = 'finance org'

    def issue_str(self, obj):
        return obj.propose.issue
    issue_str.short_description = 'заявка'

    def humanized_id(self, obj):
        return obj.id
    humanized_id.short_description = 'номер дозапроса'


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


class IFOPFormalizeDocumentInlineAdmin(TabularInline):
    extra = 1
    model = IssueFinanceOrgProposeFormalizeDocument
    show_change_link = True
    form = IFOPFormalizeDocumentInlineAdminForm
    fields = (
        'name',
        'file',
    )
    classes = ('collapse',)


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


class IFOPFinalDocumentInlineAdmin(TabularInline):
    extra = 1
    model = IssueFinanceOrgProposeFinalDocument
    show_change_link = True
    form = IFOPFinalDocumentInlineAdminForm
    fields = (
        'name',
        'file',
    )
    classes = ('collapse',)


class IFOPClarificationMessageInlineAdmin(StackedInline):
    extra = 1
    model = models.IssueFinanceOrgProposeClarificationMessage
    show_change_link = True
    formfield_overrides = {
        TextField: dict(widget=forms.Textarea(dict(rows=4)))
    }


class IssueBGProdAffiliateInlineAdmin(TabularInline):
    extra = 0
    model = IssueBGProdAffiliate
    classes = ('collapse',)


class IssueBGProdFounderLegalInlineAdmin(TabularInline):
    extra = 0
    model = IssueBGProdFounderLegal
    classes = ('collapse',)


class IssueBGProdFounderPhysicalInlineAdmin(TabularInline):
    extra = 0
    model = IssueBGProdFounderPhysical
    classes = ('collapse',)
