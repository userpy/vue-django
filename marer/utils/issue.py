from django.core.exceptions import ObjectDoesNotExist

from marer import consts
from marer.models import BankMinimalCommission


def bank_commission(bg_start_date, bg_end_date, bg_sum, bg_is_benefeciary_form, tender_has_prepayment, tender_exec_law):
    """
    Расчет банковской комиссии
    :param bg_start_date:
    :param bg_end_date:
    :param bg_sum:
    :param bg_is_benefeciary_form:
    :param tender_has_prepayment:
    :param tender_exec_law:
    :return:
    """
    Q25 = 0.0027  # Процент: 0,27% (процент чего?)
    M10 = 0.1  # Предоставление гарантии по форме заказчика: 10%
    M11 = 0.1  # Контрактом предусмотрена возможность выплаты Аванса: 10%
    M12 = 0.05  # Гарантия в рамках 185-ФЗ: 5%
    M13 = 0.1  # Гарантия качества: 10%
    M14 = 0.15  # Подтверждение опыта исполнения контрактов (более 5 документов): 15%
    M15 = 0.05  # Увеличение/продление срока контракта: 5%

    E7 = bg_start_date
    F10 = bg_sum
    F11 = bg_end_date
    F17 = bg_is_benefeciary_form
    F18 = tender_has_prepayment
    F19 = tender_exec_law == consts.TENDER_EXEC_LAW_185_FZ  # Гарантия в рамках 185-ФЗ: +/-
    F20 = False  # Гарантия качества: +/-
    F21 = False  # Подтверждение опыта исполнения контрактов (более 5 документов): +/-
    F22 = False  # Увеличение/продление срока контракта: +/-

    # F23: **Пусто**
    # M16: **Пусто**
    # M130: **Пусто**

    def _year(datetime):
        return datetime.year

    def _month(datetime):
        return datetime.month

    O25 = 1 + (_year(F11) - _year(E7)) * 12 + _month(F11) - _month(E7)
    Q17 = float(F10) * O25 * Q25
    Q22 = Q17 * (
        1
        + (M10 if F17 else 0)
        + (M11 if F18 else 0)
        + (M12 if F19 else 0)
        + (M13 if F20 else 0)
        + (M15 if F21 else 0)
        + (M14 if F22 else 0)
        # + (M130 if F20 else 0)
        # + (M16 if F23 else 0)
    )
    try:
        min_com = BankMinimalCommission.objects.get(
            sum_min__lte=bg_sum,
            sum_max__gte=bg_sum,
            term_months_min__lte=O25,
            term_months_max__gte=O25,
        )
        O24 = min_com.commission
    except ObjectDoesNotExist:
        return None

    Q20 = O24 if Q22 < O24 else Q22  # Q20: =ЕСЛИ(Q22<O24;O24;Q22)
    return round(Q20, 2)