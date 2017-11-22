import re

from cats.constants import ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE, \
    ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS

WEEKS = 'weeks'

DESCR_DATA_KEYS = (ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE)
PATTERN_SEARCH_AGE_INFO = re.compile(
    r'([-,\d]*)(([\d]+)|(года?))([ -х]*)(мес|год|нед|лет)|(возраст[ -~]*(около|до)?[ -]*года)'
)
PATTERN_AGE_NUMBER = re.compile(r"[\.\d,]+")
PATTERN_TAG = re.compile(r"#\w+_c")


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
        return ANIMAL_MONTHS
    elif 'год' in age_info or 'лет' in age_info:
        return ANIMAL_YEARS
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
                time_period = ANIMAL_DAYS
                age_number *= 7
            res[time_period] = age_number
    return res


def get_field_value_info(description):
    return None


def get_animal_tag(description):
    match = re.search(PATTERN_TAG, description)
    if match:
        tag = match.group()
        tag = tag.replace('_c', '_catsekb')
        return tag
    else:
        return None


def get_info_from_description(description):
    date_of_birth, age_precision = get_age_info(description)
    field_value_info = get_field_value_info(description)
    tag = get_animal_tag(description)
    vals = (tag, date_of_birth, age_precision, field_value_info)
    res = {key: val for key, val in zip(DESCR_DATA_KEYS, vals) if val}
    return res
