import re
from datetime import date

from cats.cats_constants import ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, \
    ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_MONTH, \
    ANIMAL_BIRTHDAY_PRECISION_YEAR, ANIMAL_SHELTER_DATE
from cats.time import get_date_from_age

WEEKS = 'weeks'

DESCR_DATA_KEYS = (ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_SHELTER_DATE)
PATTERN_SEARCH_AGE_INFO = re.compile(
    r'([-,\d]*)(([\d]+)|(года?))([ -х]*)(мес|год|нед|лет)|(возраст[ -~]*(около|до)?[ -]*года)'
)
PATTERN_AGE_NUMBER = re.compile(r"[\.\d,]+")
PATTERN_TAG = re.compile(r"(?<=#)\w+(?=_c)")


def get_number_from_string(s):
    try:
        res = float(s.replace(',', '.'))
    except ValueError:
        return None
    else:
        return res


def get_number_from_age_list(age_number_string_list):
    age_number_string = [get_number_from_string(i) for i in age_number_string_list]
    age_number_string = [i for i in age_number_string if i is not None]
    if len(age_number_string) >= 2 and age_number_string[0] < age_number_string[1]:
        res = int((age_number_string[0] + age_number_string[1]) / 2)
    else:
        try:
            res = int(age_number_string[0])
        except IndexError:
            res = None
    return res


def get_time_period(age_info):
    if 'нед' in age_info:
        return WEEKS
    elif 'мес' in age_info:
        return ANIMAL_BIRTHDAY_PRECISION_MONTH
    elif 'год' in age_info or 'лет' in age_info:
        return ANIMAL_BIRTHDAY_PRECISION_YEAR
    else:
        return None


def get_age_info(description):
    res = dict()
    age_info = re.search(PATTERN_SEARCH_AGE_INFO, description)
    if age_info:
        age_info_string = age_info.group()
        # TODO: check len(group)>1
        age_number_list = re.findall(PATTERN_AGE_NUMBER, age_info_string)
        time_period = get_time_period(age_info_string)
        if age_number_list:
            age_number = get_number_from_age_list(age_number_list)
        else:
            age_number = 1
        if time_period and age_number:
            if time_period == WEEKS:
                time_period = ANIMAL_BIRTHDAY_PRECISION_DAY
                age_number *= 7
            res[time_period] = age_number
    return res


def get_field_value_type_from_descr(description, pattern, field_vals, field_type):
    match = re.search(pattern, description)
    res = dict()
    if match:
        for pattern_value, return_value in field_vals:
            if re.search(pattern_value, description):
                res[field_type] = return_value
                break
    return res


def get_animal_tag(description):
    match = re.search(PATTERN_TAG, description)
    if match:
        tag = match.group()
        return tag
    else:
        return None


def get_precision_from_age(age):

    for precision in (
        ANIMAL_BIRTHDAY_PRECISION_DAY,
        ANIMAL_BIRTHDAY_PRECISION_MONTH,
        ANIMAL_BIRTHDAY_PRECISION_YEAR,
    ):
        if precision in age:
            return precision
    else:
        return None


def get_animal_date_of_birth(description, created_time_stamp):
    age = get_age_info(description)

    try:
        created_time_stamp = int(created_time_stamp)
    except ValueError:
        created_time_stamp = None
    if created_time_stamp is not None:
        created_date = date.fromtimestamp(created_time_stamp)
    else:
        created_date = None
    if not age:
        return None, None, created_date
    date_of_birth = get_date_from_age(
        start_date=created_date,
        years=age.get(ANIMAL_BIRTHDAY_PRECISION_YEAR, 0),
        months=age.get(ANIMAL_BIRTHDAY_PRECISION_MONTH, 0),
        days=age.get(ANIMAL_BIRTHDAY_PRECISION_DAY, 0)
    )
    age_precision = get_precision_from_age(age)
    return date_of_birth, age_precision, created_date


def get_info_from_description(description, created_time_stamp):
    animal_date_of_birth, age_precision, shelter_date = get_animal_date_of_birth(description, created_time_stamp)
    tag = get_animal_tag(description)
    vals = (tag, animal_date_of_birth, age_precision, shelter_date)
    res = {key: val for key, val in zip(DESCR_DATA_KEYS, vals) if val}
    return res
