import warnings

from django.conf import settings

from marer.models import Issue, User, IssueClarification, \
    IssueClarificationMessage
from marer.models.issue import IssueProposeDocument


def _get_default_manager():
    return User.objects.get(id=settings.DEFAULT_MANAGER_ID)


def _get_default_low_cost_manager():
    return User.objects.get(id=settings.LOW_COST_ISSUES_DEFAULT_MANAGER_ID)


def notify_user_about_manager_created_issue_for_user(issue: Issue):
    manager = issue.manager

    if manager is None:
        if issue.bg_sum > 1500000:
            manager = _get_default_manager()
        else:
            manager = _get_default_low_cost_manager()

    user = issue.user
    # менеджер создал заявку, уведомить клиента
    user.email_user(
        subject="Ваш менеджер создал Вам новую заявку",
        html_template_filename='mail/events_for_send_to_user/manager_created_new_issue_for_user.html',
        context=dict(
            manager_full_name=manager.__str__(),
            new_issue_id=issue.id,
            new_issue_number=issue.humanized_id,
            finance_product=issue.get_product().humanized_name,
            issuer_short_name=issue.issuer_short_name,
        )
    )


def notify_manager_about_user_created_issue(issue: Issue):
    manager = issue.manager
    if manager is None:
        if issue.bg_sum > 1500000:
            manager = _get_default_manager()
        else:
            manager = _get_default_low_cost_manager()

    # клиент создал заявку, уведомить менеджера
    manager.email_user(
        subject="Новая заявка от клиента",
        html_template_filename='mail/events_for_send_to_user_manager/user_created_new_issue.html',
        context=dict(
            user_full_name=issue.user.__str__(),
            new_issue_id=issue.id,
            new_issue_number=issue.humanized_id,
            finance_product=issue.get_product().humanized_name,
            issuer_short_name=issue.issuer_short_name,
        )
    )


def notify_manager_about_user_sign_document(document: IssueProposeDocument):
    issue = document.issue
    manager = issue.manager
    if manager is None:
        if issue.bg_sum > 1500000:
            manager = _get_default_manager()
        else:
            manager = _get_default_low_cost_manager()

    # клиент создал заявку, уведомить менеджера
    manager.email_user(
        subject="Клиент подписал документ",
        html_template_filename='mail/events_for_send_to_user_manager/user_sign_document.html',
        context=dict(
            user_full_name=issue.user.__str__(),
            issue_id=issue.id,
            issue_number=issue.humanized_id,
            finance_product=issue.get_product().humanized_name,
            issuer_short_name=issue.issuer_short_name,
            document_name=document.name,
        )
    )


def notify_user_about_manager_updated_issue_for_user(issue: Issue):
    # DISABLED
    # user_manager = issue.user.manager
    # if user_manager is None:
    #     user_manager = _get_default_manager()
    #
    # user = issue.user
    # # менеджер пользователя изменил заявку, уведомить клиента
    # user.email_user(
    #     subject="Ваш менеджер изменил Вашу заявку",
    #     html_template_filename='mail/events_for_send_to_user/manager_updated_issue_for_user.html',
    #     context=dict(
    #         manager_full_name=user_manager.__str__(),
    #         issue_id=issue.id,
    #         issue_number=issue.humanized_id,
    #         finance_product=issue.get_product().humanized_name,
    #         issuer_short_name=issue.issuer_short_name,
    #     )
    # )
    pass


def notify_manager_about_user_updated_issue(issue: Issue):
    manager = issue.manager
    if manager is None:
        if issue.bg_sum > 1500000:
            manager = _get_default_manager()
        else:
            manager = _get_default_low_cost_manager()

    # клиент создал заявку, уведомить менеджера
    manager.email_user(
        subject="Клиент изменил заявку",
        html_template_filename='mail/events_for_send_to_user_manager/user_updated_issue.html',
        context=dict(
            user_full_name=issue.user.__str__(),
            issue_id=issue.id,
            issue_number=issue.humanized_id,
            finance_product=issue.get_product().humanized_name,
            issuer_short_name=issue.issuer_short_name,
        )
    )


def notify_manager_about_new_issue(issue: Issue):
    manager = issue.manager
    if manager is None:
        if issue.bg_sum > 1500000:
            manager = _get_default_manager()
        else:
            manager = _get_default_low_cost_manager()

    manager.email_user(
        subject='Новая заявка',
        html_template_filename='mail/events_for_send_to_fo_manager/new_issue.html',
        context=dict(
            issue_number=issue.humanized_id,
            issue_id=issue.id,
            finance_product=issue.get_product().humanized_name,
            issuer_short_name=issue.issuer_short_name
        )
    )


def notify_managers_issue_in_review(issue: Issue):
    """
    Заявка перешла в статус рассмотрение
    :param issue:
    """
    # клиент отправил заявку на рассмотрение, уведомить менеджера
    if issue.manager:
        issue.manager.email_user(
            subject="Заявка перешла в статус 'рассмотрение'",
            html_template_filename='mail/events_for_send_to_user_manager/issue_in_review.html',
            context=dict(
                user_full_name=issue.user.__str__(),
                issue_id=issue.id,
                issue_number=issue.humanized_id,
                finance_product=issue.get_product().humanized_name,
                issuer_short_name=issue.issuer_short_name,
            )
        )


def notify_about_user_created_clarification(clarification: IssueClarification):
    # notify user manager and fo manager

    # DISABLED
    # user_manager = clarification.propose.issue.user.manager
    # if user_manager is None:
    #     user_manager = _get_default_manager()
    #
    # user_manager.email_user(
    #     subject="Пользователь создал новый дозапрос по заявке",
    #     html_template_filename='mail/events_for_send_to_user/.html',
    #     context=dict(
    #         # user_full_name=propose.issue.user.__str__(),
    #         # issue_id=propose.issue.id,
    #         # issue_number=propose.issue.humanized_id,
    #         # finance_product=propose.issue.get_product().humanized_name,
    #         # issuer_short_name=propose.issue.issuer_short_name,
    #     )
    # )

    # if not clarification.propose.finance_org.manager_id:
    #     warnings.warn('No manager for FO #{org_id} got notify of clarification for propose #{propose_id}'.format(
    #         org_id=clarification.propose.finance_org.id,
    #         propose_id=clarification.propose_id,
    #     ))
    # else:
    #     clarification.propose.finance_org.manager.email_user(
    #         subject="Пользователь создал новый дозапрос по заявке",
    #         html_template_filename='mail/events_for_send_to_fo_manager/user_created_clarification.html',
    #         context=dict(
    #             user_full_name=clarification.propose.issue.user.__str__(),
    #             issue_id=clarification.propose.issue.id,
    #             issue_number=clarification.propose.issue.humanized_id,
    #             finance_product=clarification.propose.issue.get_product().humanized_name,
    #             issuer_short_name=clarification.propose.issue.issuer_short_name,
    #             finance_org_name=clarification.propose.finance_org.name,
    #             clarification_id=clarification.id,
    #         )
    #     )

    warnings.warn('Clarification {} is saved but nobody notified'.format(clarification.id))


def notify_about_user_adds_message(msg: IssueClarificationMessage):
    # notify fo manager and user manager

    # DISABLED
    # user_manager = msg.clarification.propose.issue.user.manager
    # if user_manager is None:
    #     user_manager = _get_default_manager()
    #
    # user_manager.email_user(
    #     subject="Пользователь добавил сообщение по дозапросу в заявке",
    #     html_template_filename='mail/events_for_send_to_user/.html',
    #     context=dict(
    #         # user_full_name=propose.issue.user.__str__(),
    #         # issue_id=propose.issue.id,
    #         # issue_number=propose.issue.humanized_id,
    #         # finance_product=propose.issue.get_product().humanized_name,
    #         # issuer_short_name=propose.issue.issuer_short_name,
    #     )
    # )

    if not msg.clarification.propose.finance_org.manager_id:
        warnings.warn('No manager for FO #{org_id} got notify of clarification for propose #{propose_id}'.format(
            org_id=msg.clarification.propose.finance_org.id,
            propose_id=msg.clarification.propose_id,
        ))
    else:
        msg.clarification.propose.finance_org.manager.email_user(
            subject="Менеджер клиента оставил новое сообщение по дозапросу к заявке в Ваш банк",
            html_template_filename='mail/events_for_send_to_fo_manager/user_added_clarification_message.html',
            context=dict(
                user_full_name=msg.clarification.propose.issue.user.__str__(),
                issue_id=msg.clarification.propose.issue.id,
                issue_number=msg.clarification.propose.issue.humanized_id,
                finance_product=msg.clarification.propose.issue.get_product().humanized_name,
                issuer_short_name=msg.clarification.propose.issue.issuer_short_name,
                finance_org_name=msg.clarification.propose.finance_org.name,
                clarification_id=msg.clarification.id,
            )
        )


def notify_managers_about_new_message_in_chat(message: IssueClarificationMessage):
    author_role = 'Агент' if message.user == message.issue.user else 'Менеджер банка'
    context = dict(
        author_role=author_role,
        issue_number=message.issue.humanized_id,
        issue_id=message.issue.id,
        finance_product=message.issue.get_product().humanized_name,
        issuer_short_name=message.issue.issuer_short_name,
    )
    subject = '%s добавил сообщение по дозапросу к заявке' % author_role
    if message.user == message.issue.user:
        if message.issue.manager:
            message.issue.manager.email_user(
                subject=subject,
                html_template_filename='mail/events_for_send_to_user_manager/new_message_in_chat.html',
                context=context
            )
    else:
        message.issue.user.email_user(
            subject=subject,
            html_template_filename='mail/events_for_send_to_user/new_message_in_chat.html',
            context=context
        )
