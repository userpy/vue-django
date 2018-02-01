
ISSUE_STATUS_REGISTERING = 'registering'
ISSUE_STATUS_REVIEW = 'review'
ISSUE_STATUS_FINISHED = 'finished'
ISSUE_STATUS_CANCELLED = 'cancelled'
ISSUE_STATUS_CLIENT_REVISION = 'client_revision'
ISSUE_STATUS_RETURNED_FROM_REVISION = 'returned_from_revision'
ISSUE_STATUS_CLIENT_AGGREEMENT = 'client_agreement'
ISSUE_STATUS_CANCELLED_BY_CLIENT = 'cancelled_by_client'

TENDER_EXEC_LAW_44_FZ = '44-fz'
TENDER_EXEC_LAW_223_FZ = '223-fz'
TENDER_EXEC_LAW_185_FZ = '185-fz'
TENDER_EXEC_LAW_COMMERCIAL = 'commercial'
TENDER_EXEC_LAW_CUSTOMS = 'customs'
TENDER_EXEC_LAW_VAT = 'vat'

TENDER_CONTRACT_TYPE_SUPPLY_CONTRACT = 'supply'
TENDER_CONTRACT_TYPE_SERVICE_CONTRACT = 'service'
TENDER_CONTRACT_TYPE_WORKS_CONTRACT = 'works'

BG_TYPE_APPLICATION_ENSURE = 'application_ensure'
BG_TYPE_CONTRACT_EXECUTION = 'contract_execution'
BG_TYPE_WARRANTY_ENSURE = 'warranty_ensure'
BG_TYPE_REFUND_OF_ADVANCE = 'refund_of_advance'

TAX_USN = 'tax_usn'
TAX_OSN = 'tax_osn'
TAX_ENVD = 'tax_envd'
TAX_ESHD = 'tax_eshd'

CURRENCY_RUR = 'rur'
CURRENCY_USD = 'usd'
CURRENCY_EUR = 'eur'

IFOPC_INITIATOR_FINANCE_ORG = 'finance_org'
IFOPC_INITIATOR_ISSUER = 'issuer'

ISSUE_CREDIT_REPAYMENT_SCHEDULE_EQUAL_SHARES = 'equal_shares'
ISSUE_CREDIT_REPAYMENT_SCHEDULE_END_OF_TERM = 'end_of_term'

ISSUE_DEAL_BANK_RELATIONS_TERM_SHORT = 'short_term'
ISSUE_DEAL_BANK_RELATIONS_TERM_LONG = 'long_term'

ISSUE_ISSUER_ACTIVITY_OBJECTIVE_PROFIT_MAKING = 'profit_making'
ISSUE_ISSUER_ACTIVITY_OBJECTIVE_OTHER = 'other'

ISSUE_ISSUER_FINANCE_SITUATION_SATISFIED = 'satisfied'
ISSUE_ISSUER_FINANCE_SITUATION_UNSATISFIED = 'unsatisfied'

ISSUE_ISSUER_BUSINESS_REPUTATION_POSITIVE = 'positive'
ISSUE_ISSUER_BUSINESS_REPUTATION_NOT_PRESENT = 'not_present'

ISSUER_FUNDS_SOURCE_LOAN_FUNDS = 'loan_funds'
ISSUER_FUNDS_SOURCE_OTHER = 'other'

CREDIT_PLEDGE_TYPE_DEPOSIT = 'deposit'
CREDIT_PLEDGE_TYPE_REAL_ESTATE = 'real_estate'
CREDIT_PLEDGE_TYPE_OTHER = 'other'

FO_PRODUCT_CONDITIONS_INSURANCE_TYPE_REAL_ESTATE = 'real_estate'
FO_PRODUCT_CONDITIONS_INSURANCE_TYPE_PLEDGE = 'pledge'

FO_PRODUCT_PROPOSE_DOC_HEAD_PASSPORT = 'head_passport'
FO_PRODUCT_PROPOSE_DOC_HEAD_STATUTE = 'statute'

DOCUMENT_TYPE_LEGAL = 1
DOCUMENT_TYPE_FINANCE = 2
DOCUMENT_TYPE_OTHER = 3
DOCUMENT_TYPE_CHOICES = (
    (DOCUMENT_TYPE_LEGAL, 'Юридические документы'),
    (DOCUMENT_TYPE_FINANCE, 'Финансовые документы'),
    (DOCUMENT_TYPE_OTHER, 'Прочее'),
)

CREDIT_PURPOSE_TYPE_CONTRACT_EXEC = 'contract_exec'
CREDIT_PURPOSE_TYPE_WORK_CAPITAL_REFILL = 'work_capital_refill'

DOCUMENT_SIGN_VERIFIED = 'verified'
DOCUMENT_SIGN_CORRUPTED = 'corrupted'
DOCUMENT_SIGN_NONE = 'none'

DOCUMENT_SIGN_LABELS = {
    DOCUMENT_SIGN_VERIFIED: 'Проверена',
    DOCUMENT_SIGN_CORRUPTED: 'Неверна',
    DOCUMENT_SIGN_NONE: 'Отсутствует',
}
