from django.contrib.admin import StackedInline, TabularInline
from django import forms
from django.db.models import TextField
from django.forms import Select

from marer import models
from marer.forms.widgets import ReadOnlyFileInput
from marer.models import Document
from marer.models.finance_org import FinanceOrgProductProposeDocument
from marer.models.issue import IssueFinanceOrgProposeFormalizeDocument, IssueFinanceOrgProposeFinalDocument, \
    IssueBGProdAffiliate, IssueBGProdFounderLegal, IssueBGProdFounderPhysical, IssueCreditPledge


class IssueFinanceOrgProposeInlineAdmin(StackedInline):
    extra = 1
    model = models.IssueFinanceOrgPropose
    fields = ('finance_org',)
    show_change_link = True
    can_delete = False

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)


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
        if obj is not None:
            choices = [(ch.code, ch.name) for ch in obj.get_product().get_documents_list()]
            self.form.declared_fields['code'].widget.choices = choices
        return super().get_formset(request, obj, **kwargs)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_delete_permission(request, obj)


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

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.change_issuefinanceorgproposeclarification'):
            pass
        elif request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.issue.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            if obj is None:
                return True
            elif obj.finance_org.manager_id == request.user.id:
                return True
        return super().has_change_permission(request, obj)

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

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.change_issuefinanceorgproposeformalizedocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_users_issues'):
            # todo make it read only
            if obj is None:
                return True
            elif obj.issue.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            if obj is None:
                return True
            elif obj.finance_org.manager_id == request.user.id:
                return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.change_issuefinanceorgproposeformalizedocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            return True
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.change_issuefinanceorgproposeformalizedocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            if obj is None:
                return True
            elif obj.finance_org.manager_id == request.user.id:
                return True
        return super().has_delete_permission(request, obj)


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

    # todo check add permission
    # todo check del permission

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.change_issuefinanceorgproposefinaldocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_users_issues'):
            # todo make it read only
            if obj is None:
                return True
            elif obj.issue.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            if obj is None:
                return True
            elif obj.finance_org.manager_id == request.user.id:
                return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.change_issuefinanceorgproposeformalizedocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            return True
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.change_issuefinanceorgproposeformalizedocument'):
            pass
        elif request.user.has_perm('marer.can_change_managed_finance_org_proposes'):
            if obj is None:
                return True
            elif obj.finance_org.manager_id == request.user.id:
                return True
        return super().has_delete_permission(request, obj)


class FinanceOrgProductProposeDocumentInlineAdminForm(forms.ModelForm):
    file = forms.FileField(required=False, label='файл', widget=ReadOnlyFileInput)

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


class FinanceOrgProductProposeDocumentInlineAdmin(TabularInline):
    extra = 1
    model = FinanceOrgProductProposeDocument
    show_change_link = True
    form = FinanceOrgProductProposeDocumentInlineAdminForm
    fields = (
        'name',
        'finance_product',
        'code',
        'file',
    )
    classes = ('collapse',)

    # todo check add permission
    # todo check change permission
    # todo check del permission


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

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_delete_permission(request, obj)


class IssueBGProdFounderLegalInlineAdmin(TabularInline):
    extra = 0
    model = IssueBGProdFounderLegal
    classes = ('collapse',)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_delete_permission(request, obj)


class IssueBGProdFounderPhysicalInlineAdmin(TabularInline):
    extra = 0
    model = IssueBGProdFounderPhysical
    classes = ('collapse',)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_delete_permission(request, obj)


class IssueCreditPledgeInlineAdmin(TabularInline):
    extra = 0
    model = IssueCreditPledge
    classes = ('collapse',)

    def has_add_permission(self, request):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            if obj is None:
                return True
            elif obj.user.manager_id == request.user.id:
                return True
        elif request.user.has_perm('marer.can_view_managed_finance_org_proposes_issues'):
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('marer.can_change_managed_users_issues'):
            return True
        return super().has_delete_permission(request, obj)
