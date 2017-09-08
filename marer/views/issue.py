from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from marer.forms import IssueRegisteringForm
from marer.models import Issue, Issuer
from marer.views import StaticPagesContextMixin


class IssueView(LoginRequiredMixin, TemplateView, StaticPagesContextMixin):
    template_name = ''
    _issue = None

    def get_issue(self):
        if self._issue is not None:
            return self._issue

        iid = self.kwargs.get('iid', None)
        if iid is not None:
            # fixme maybe make error 403?
            issue = get_object_or_404(Issue, id=iid, user_id=self.request.user.id)
            self._issue = issue
            return issue

    def get_context_data(self, **kwargs):
        kwargs.update(dict(issue=self.get_issue()))
        return super().get_context_data(**kwargs)


class IssueRedirectView(RedirectView):
    permanent = False

    def get(self, request, *args, **kwargs):
        iid = kwargs.get('iid', None)
        issue = None
        if iid is not None:
            # fixme maybe make error 403?
            issue = get_object_or_404(Issue, id=iid, user_id=request.user.id)

        if issue.status == Issue.STATUS_REGISTERING:
            self.pattern_name = 'issue_registering'
        elif issue.status == Issue.STATUS_COMMON_DOCUMENTS_REQUEST:
            self.pattern_name = 'issue_common_documents_request'
        elif issue.status == Issue.STATUS_SURVEY:
            self.pattern_name = 'issue_survey'
        elif issue.status == Issue.STATUS_SCORING:
            self.pattern_name = 'issue_scoring'
        elif issue.status == Issue.STATUS_ADDITIONAL_DOCUMENTS_REQUEST:
            self.pattern_name = 'issue_additional_documents_request'
        elif issue.status == Issue.STATUS_PAYMENTS:
            self.pattern_name = 'issue_payments'
        elif issue.status == Issue.STATUS_FINAL_DOCUMENTS_APPROVAL:
            self.pattern_name = 'issue_final_documents_approval'
        elif issue.status == Issue.STATUS_FINISHED:
            self.pattern_name = 'issue_finished'
        elif issue.status == Issue.STATUS_CANCELLED:
            self.pattern_name = 'issue_cancelled'

        return super().get(request, *args, **kwargs)


class IssueRegisteringView(IssueView):
    template_name = 'marer/issue/registering.html'

    def get(self, request, *args, **kwargs):
        if 'base_form' not in kwargs:
            if self.get_issue():
                initial = dict(
                    product=self.get_issue().product,
                    org_search_name=self.get_issue().get_issuer_name(),
                    comment=self.get_issue().comment,
                )
            else:
                initial = dict()
            base_form = IssueRegisteringForm(initial=initial)
            kwargs.update(dict(base_form=base_form))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        base_form = IssueRegisteringForm(request.POST)
        if base_form.is_valid():
            # todo go to next stage if we can
            if not self.get_issue():
                issuer_name = base_form.cleaned_data['org_search_name']
                issuer = Issuer(
                    full_name=issuer_name,
                    short_name=issuer_name,
                    inn='0000000000',
                    kpp='000000000',
                    ogrn='0000000000000',
                    user=request.user,
                )
                issuer.save()

                new_issue = Issue(
                    issuer=issuer,
                    product=base_form.cleaned_data['product'],
                    status=Issue.STATUS_REGISTERING,
                    user=request.user,
                )  # todo set values
                new_issue.fill_from_issuer()
                self._issue = new_issue
            issue = self.get_issue()
            issue.comment = base_form.cleaned_data['comment']
            issue.save()
        kwargs.update(dict(base_form=base_form))
        return self.get(request, *args, **kwargs)


class IssueCommonDocumentsRequestView(IssueView):
    template_name = 'marer/issue/common_documents_request.html'

    def get(self, request, *args, **kwargs):
        fp_documents = self.get_issue().get_product().get_documents_list()
        fp_docs_codes = [fpd.code for fpd in fp_documents]
        issue_documents = self.get_issue().common_documents.filter(code__in=fp_docs_codes)
        for idoc in issue_documents:
            for fp in fp_documents:
                if idoc.code == fp.code:
                    fp.set_document(idoc.document)
        kwargs.update(dict(documents=fp_documents))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        fp_documents = self.get_issue().get_product().get_documents_list()
        for fpdoc in fp_documents:
            post_file = request.FILES.get(fpdoc.code, None)
            if post_file is not None:
                self.get_issue().update_common_issue_doc(fpdoc.code, post_file)
        return self.get(request, *args, **kwargs)


class IssueSurveyView(IssueView):
    template_name = 'marer/issue/survey.html'


class IssueScoringView(IssueView):
    template_name = 'marer/issue/scoring.html'


class IssueAdditionalDocumentsRequestsView(IssueView):
    template_name = 'marer/issue/additional_documents_requests.html'


class IssueAdditionalDocumentsRequestView(IssueView):
    template_name = 'marer/issue/additional_documents_request.html'


class IssuePaymentsView(IssueView):
    template_name = 'marer/issue/payments.html'


class IssueFinishedView(IssueView):
    template_name = 'marer/issue/finished.html'


class IssueCancelledView(IssueView):
    template_name = 'marer/issue/cancelled.html'
