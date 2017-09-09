# TODO: delete this file
from dateutil.relativedelta import relativedelta
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
    later = later_date

    before = before_date
    mode = YEARLY
    result[YEARS] = get_calendar_items_count(before, mode, later)


    mode = MONTHLY
    if later_date >= before_date + relativedelta(years=result[YEARS]):
        m = 'Др наступила! ДР:{}, ДАТА:{}'
        print(m.format(before_date, later_date))
    else:
        m = 'Др не наступила! ДР:{}, ДАТА:{}'
        print(m.format(before_date, later_date))




    #     # before = date(later_date.year, before_date.month, before_date.day) - relativedelta(years=1)
    #     before = before_date + relativedelta(years=result[YEARS]+1)
    #     result[MONTHS] = get_calendar_items_count(before, mode, later)
    # elif later_date.month > before_date.month:
    #     before = date(later_date.year, before_date.month, before_date.day)
    #     result[MONTHS] = get_calendar_items_count(before, mode, later)
    # else:
    #     result[MONTHS] = None
    #
    # mode = DAILY
    # if later_date.day < before_date.day:
    #     before = date(later_date.year, later_date.month, before_date.day) - relativedelta(months=1)
    #
    #     result[DAYS] = get_calendar_items_count(before, mode, later)
    #     if result[MONTHS] is None:
    #         mode = MONTHLY
    #         before = date(later_date.year, before_date.month, before_date.day) - relativedelta(years=1)
    #         result[MONTHS] = get_calendar_items_count(before, mode, later)
    # elif later_date.day > before_date.day:
    #     before = date(later_date.year, later_date.month, before_date.day)
    #     result[DAYS] = get_calendar_items_count(before, mode, later)
    #     if result[MONTHS] is None:
    #         mode = MONTHLY
    #         before = date(later_date.year, later_date.month, before_date.day)
    #         result[MONTHS] = get_calendar_items_count(before, mode, later)
    # else:
    #     before = date(later_date.year, later_date.month, before_date.day)
    #     result[DAYS] = get_calendar_items_count(before, mode, later)
    #     if result[MONTHS] is None:
    #         mode = MONTHLY
    #         before = date(later_date.year, later_date.month, before_date.day)
    #         result[MONTHS] = get_calendar_items_count(before, mode, later) + 1


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


# def get_date(year, month, day):
#     try:
#         res = date(year, month, day)
#     except ValueError as e:
#         if 'day is out of range for month' == e.args[0]:
#             return get_date(year, month, day-1)
#     else:
#         return res



