# TODO: delete this file

# dateutil using
from dateutil.rrule import rrule, MONTHLY, YEARLY, DAILY
from datetime import date, timedelta


YEARS = 'years'
MONTHS = 'months'
DAYS = 'days'


def calc_age_uptoday(before_date, later_date):
    """

    :type before_date: date
    :type later_date: date
    """
    result = dict()
    result[YEARS] = rrule(YEARLY, dtstart=before_date, until=later_date).count() - 1
    if later_date.month < before_date.month:
        # Месяц дня рождения еще не наступил
        result[MONTHS] = rrule(
            MONTHLY,
            dtstart=date(later_date.year-1, before_date.month, before_date.day),
            until=later_date
        ).count() - 1
    elif later_date.month > before_date.month:
        # Месяц дня рождения прошел
        result[MONTHS] = rrule(
            MONTHLY,
            dtstart=date(later_date.year, before_date.month, before_date.day),
            until=later_date
        ).count() - 1
    else:
        # Месяц дня рождения
        result[MONTHS] = None

    if later_date.day < before_date.day:
        result[DAYS] = rrule(
            DAILY,
            dtstart=date(later_date.year, before_date.month-1, before_date.day),
            until=later_date
        ).count() - 1
        if result[MONTHS] is None:
            # Месяц ДР, до дня ДР
            result[MONTHS] = rrule(
                MONTHLY,
                dtstart=date(later_date.year - 1, before_date.month, before_date.day),
                until=later_date
            ).count() - 1

    elif later_date.day >= before_date.day:
        result[DAYS] = rrule(
            DAILY,
            dtstart=date(later_date.year, later_date.month, before_date.day),
            until=later_date
        ).count() - 1
        if result[MONTHS] is None:
            # Месяц ДР, во время и после дня ДР
            result[MONTHS] = rrule(
                MONTHLY,
                dtstart=date(later_date.year, before_date.month, before_date.day),
                until=later_date
            ).count() - 1
    return result




