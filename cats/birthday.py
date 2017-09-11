# TODO: delete this file
from datetime import date

from dateutil.relativedelta import relativedelta

YEARS = 'years'
MONTHS = 'months'
DAYS = 'days'


def calc_age_uptoday(before_date, later_date):
    """

    :type before_date: date
    :type later_date: date
    """

    result = dict()
    diff = relativedelta(later_date, before_date)
    result[YEARS] = diff.years
    result[MONTHS] = diff.months
    result[DAYS] = diff.days
    return result
