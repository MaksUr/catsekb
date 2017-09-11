# TODO: delete this file
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY, YEARLY, DAILY
from datetime import date
from calendar import monthrange



YEARS = 'years'
MONTHS = 'months'
DAYS = 'days'


def calc_age_uptoday(before_date, later_date):
    """

    :type before_date: date
    :type later_date: date
    """
    result = dict()
    later = later_date

    before = before_date
    mode = YEARLY
    result[YEARS] = get_calendar_items_count(before, mode, later)

    mode = MONTHLY
    before = before_date + relativedelta(years=result[YEARS])
    result[MONTHS] = get_calendar_items_count(before, mode, later)

    mode = DAILY  # Вычесление количества дней
    if later_date.day < before_date.day:
        before = later_date - relativedelta(months=1)  # Сдвиг на месяц назад сегодняшней даты
        before = get_date(before.year, before.month, before_date.day)   # Установить день месяца рождения
    else:
        before = later_date  # Получение даты дня рождения в этом гоу
        before = get_date(before.year, before.month, before_date.day)   # Установить день месяца рождения
    result[DAYS] = get_calendar_items_count(before, mode, later)
    if result[DAYS] < 0:
        result[DAYS] = 1
    else:
        month_days_count = monthrange(later_date.year, later_date.month)[1]
        if (before_date.day > later_date.day) and before_date.day > month_days_count:
            pass
        elif month_days_count <= result[DAYS]:
            result[DAYS] = 0

    return result


def disclosure_dates(dtstart, rd, dtend):
    """

    :type rd: relativedelta
    :type dtend: date
    :type dtstart: date
    """
    if dtstart > dtend:
        message = 'dtstart={start} is before dtend={end}.'
        raise ValueError(message.format(start=str(dtstart), end=str(dtend)))
    ii = 1
    while True:
        cdate = dtstart + ii*rd
        if cdate > dtend:
            return ii
        elif cdate == dtend:
            return ii+1
        ii += 1


def get_calendar_items_count(dtstart, mode, until):
    if mode == YEARLY:
        rd = relativedelta(years=1)
    elif mode == MONTHLY:
        rd = relativedelta(months=1)
    else:  #elif mode == DAILY:
        rd = relativedelta(days=1)
    res = disclosure_dates(dtstart, rd, until) - 1  # TODO: change disclosure_dates
    # TODO: use relative delta
    # res = rrule(mode, dtstart=dtstart, until=until).count() - 1
    return res


def get_date(year, month, day):
    try:
        res = date(year, month, day)
    except ValueError as e:
        if 'day is out of range for month' == e.args[0]:
            return get_date(year, month, day-1)
    else:
        return res



