# TODO: delete this file

from dateutil.rrule import rrule, MONTHLY, YEARLY, DAILY
from datetime import date


YEARS = 'years'
MONTHS = 'months'
DAYS = 'days'


def calc_age_uptoday(before_date, later_date):
    """

    :type before_date: date
    :type later_date: date
    """
    result = dict()
    result[YEARS] = get_calendar_items_count(before_date, YEARLY, later_date)
    if later_date.month < before_date.month:
        # Месяц дня рождения еще не наступил
        dtstart = get_date(later_date.year-1, before_date.month, before_date.day)
        until = later_date
        mode = MONTHLY
        result[MONTHS] = get_calendar_items_count(dtstart, mode, until)
    elif later_date.month > before_date.month:
        # Месяц дня рождения прошел
        dtstart = get_date(later_date.year, before_date.month, before_date.day)
        until = later_date
        mode = MONTHLY
        result[MONTHS] = get_calendar_items_count(dtstart, mode, until)
    else:
        # Месяц дня рождения
        result[MONTHS] = None

    if later_date.day < before_date.day:
        dtstart = get_date(later_date.year, before_date.month-1, before_date.day)
        until = later_date
        mode = DAILY
        result[DAYS] = get_calendar_items_count(dtstart, mode, until)
        if result[MONTHS] is None:
            # Месяц ДР, до дня ДР
            dtstart = get_date(later_date.year - 1, before_date.month, before_date.day)
            until = later_date
            mode = MONTHLY
            result[MONTHS] = get_calendar_items_count(dtstart, mode, until)

    elif later_date.day >= before_date.day:
        dtstart = get_date(later_date.year, later_date.month, before_date.day)
        until = later_date
        mode = DAILY
        result[DAYS] = get_calendar_items_count(dtstart, mode, until)
        if result[MONTHS] is None:
            # Месяц ДР, во время и после дня ДР
            dtstart = get_date(later_date.year, before_date.month, before_date.day)
            until = later_date
            mode = MONTHLY
            result[MONTHS] = get_calendar_items_count(dtstart, mode, until)
    return result


def get_calendar_items_count(dtstart, mode, until):
    # TODO: use relative delta
    res = rrule(mode, dtstart=dtstart, until=until).count() - 1
    return res


def get_date(year, month, day):
    try:
        res = date(year, month, day)
    except ValueError as e:
        if 'day is out of range for month' == e.args[0]:
            return get_date(year, month, day-1)
    else:
        return res



