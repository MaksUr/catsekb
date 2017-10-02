from datetime import date

from dateutil.relativedelta import relativedelta

from cats.constants import ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS


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


def get_date_from_age(years=0, months=0, days=0):

    """

    :type days: int
    :type months: int
    :type years: int
    """
    diff = relativedelta(years=years, months=months, days=days)
    return date.today() - diff


def get_age_from_string(age_string):
    """

    :type age_string: str
    """
    # TODO: parsing string
    result = dict()
    result[ANIMAL_YEARS] = 1
    result[ANIMAL_MONTHS] = 4
    result[ANIMAL_DAYS] = 5
    return result



