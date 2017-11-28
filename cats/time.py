from datetime import date

import re
from dateutil.relativedelta import relativedelta

from cats.constants import ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS

PATTERN_SEARCH_YEARS_AGE = re.compile(r'(?<=y)(?P<years>\d+)')
PATTERN_SEARCH_MONTHS_AGE = re.compile(r'(?<=m)(?P<months>\d+)')
PATTERN_SEARCH_DAYS_AGE = re.compile(r'(?<=d)(?P<days>\d+)')


def calc_age_uptoday(before_date, later_date):
    """

    :type before_date: date
    :type later_date: date
    """

    result = dict()
    diff = relativedelta(later_date, before_date)
    result[ANIMAL_YEARS] = diff.years
    result[ANIMAL_MONTHS] = diff.months
    result[ANIMAL_DAYS] = diff.days
    return result


def get_date_from_age(years=0, months=0, days=0, start_date=None):

    """

    :type start_date: date
    :param start_date: 
    :type days: int
    :type months: int
    :type years: int
    """
    diff = relativedelta(years=years, months=months, days=days)
    if start_date is None:
        start_date = date.today()
    return start_date - diff


def get_age_from_string(age_string):
    """

    :type age_string: str
    """
    def update_res(key, res, pattern, s):
        s = re.search(pattern, s)
        if s:
            try:
                v = int(s.group(key))
            except ValueError:
                pass
            else:
                res[key] = v
    result = dict()
    update_res(ANIMAL_YEARS, result, PATTERN_SEARCH_YEARS_AGE, age_string)
    update_res(ANIMAL_MONTHS, result, PATTERN_SEARCH_MONTHS_AGE, age_string)
    update_res(ANIMAL_DAYS, result, PATTERN_SEARCH_DAYS_AGE, age_string)
    return result





