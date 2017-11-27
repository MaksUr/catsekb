import re

from datetime import date

from cats.constants import ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE, \
    ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_MONTH, \
    ANIMAL_BIRTHDAY_PRECISION_YEAR, FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_A, \
    FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_C, \
    FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_B, FIELD_TYPE_INST_LITTER_BOX_SKILL, \
    FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_A, FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_C, \
    FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_B, FIELD_TYPE_INST_RELATIONSHIPS_WITH_PEOPLE, \
    FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_A, FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_B, \
    FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_C, FIELD_TYPE_INST_RELATIONSHIPS_WITH_ANIMALS, ANIMAL_DAYS, \
    ANIMAL_MONTHS, ANIMAL_YEARS
from cats.time import get_date_from_age

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


PATTERN_LITTER_BOX = re.compile(r"(([\w]+)([\W]*)){2}лото?к(ом)?(([\W]*)([\w]+)){3}")
PATTERN_LITTER_BOX_SKILL_LEVEL_A = re.compile(r"((без (промах|пробл))|лоток с |отличн|идеальн)")
PATTERN_LITTER_BOX_SKILL_LEVEL_B = re.compile(r"будет приучен")
PATTERN_LITTER_BOX_SKILL_LEVEL_C = re.compile(r"(плох|пробл|не ходит|мимо|не попад|гадит)")


def get_litter_box_skill(description):
    return get_field_value_type_from_descr(
        description=description,
        pattern=PATTERN_LITTER_BOX,
        field_vals=(
            (PATTERN_LITTER_BOX_SKILL_LEVEL_A, FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_A),
            (PATTERN_LITTER_BOX_SKILL_LEVEL_B, FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_B),
            (PATTERN_LITTER_BOX_SKILL_LEVEL_C, FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_C),
        ),
        field_type=FIELD_TYPE_INST_LITTER_BOX_SKILL
    )


PATTERN_RELATIONSHIPS_WITH_PEOPLE = re.compile(r"([кс][ ]+)(люд|чел)(\w*)(([\W]*)([\w]+)){4}")
PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_A = re.compile(r"(неж|спок|ласк|мурч|обним|добр|(?<!не) люби)")
PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_B = re.compile(r"(трус|бо(як|ит)|скром)|не люби")
PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_C = re.compile(r"(подчин|с характ|не даст|насторож)")


def get_relationships_with_people(description):
    return get_field_value_type_from_descr(
        description=description,
        pattern=PATTERN_RELATIONSHIPS_WITH_PEOPLE,
        field_vals=(
            (PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_A, FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_A),
            (PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_B, FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_B),
            (PATTERN_RELATIONSHIPS_WITH_PEOPLE_VAL_C, FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_C),
        ),
        field_type=FIELD_TYPE_INST_RELATIONSHIPS_WITH_PEOPLE
    )


PATTERN_RELATIONSHIPS_WITH_ANIMALS = re.compile(
    r"(([\w]+)([\W]*)){4}([кс])([ ]+)(другими?[ ]+)?((ко[шт])|(жив)[\w]+)(([\W]*)([\w]+)){4}"
)

PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_A = re.compile(
    r"(хор|не боит|ужив|друж|нормально|отличн|не конф|спок|ладит|((?<!не) (нашел|нашла|находит) общий язык)|(?<!не) (люби|адекв))")
PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_B = re.compile(
    r"(стрес|бо(ит|яз)|сторон)|боит|опас[ка]"
)
PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_C = re.compile(
    r"(домин|с характ|не даст|насторож|конфл|актив|(не (нашел|нашла|находит) общий язык)|убий|не люби)"
)


def get_relationships_with_animals(description):
    # TODO: check patterns
    return get_field_value_type_from_descr(
        description=description,
        pattern=PATTERN_RELATIONSHIPS_WITH_ANIMALS,
        field_vals=(
            (PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_A, FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_A),
            (PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_B, FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_B),
            (PATTERN_RELATIONSHIPS_WITH_ANIMALS_VAL_C, FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_C),
        ),
        field_type=FIELD_TYPE_INST_RELATIONSHIPS_WITH_ANIMALS
    )


def get_field_value_info(description):
    res = dict()
    res.update(get_litter_box_skill(description))
    res.update(get_relationships_with_people(description))
    return res


def get_animal_tag(description):
    match = re.search(PATTERN_TAG, description)
    if match:
        tag = match.group()
        tag = tag.replace('_c', '_catsekb')
        return tag
    else:
        return None


def get_precision_from_age(age):
    if age.get[ANIMAL_DAYS] is not None:
        return ANIMAL_BIRTHDAY_PRECISION_DAY
    elif age.get[ANIMAL_MONTHS] is not None:
        return ANIMAL_BIRTHDAY_PRECISION_MONTH
    elif age.get[ANIMAL_YEARS] is not None:
        return ANIMAL_BIRTHDAY_PRECISION_YEAR
    else:
        return None


def get_animal_date_of_birth(description, created_time_stamp):
    age = get_age_info(description)
    if created_time_stamp is not None:
        # TODO: check time stamp
        created_date = date.fromtimestamp(created_time_stamp)
    else:
        created_date = None
    date_of_birth = get_date_from_age(start_date=created_date, **age)
    age_precision = get_precision_from_age(age)
    return date_of_birth, age_precision


def get_info_from_description(description, created_time_stamp):
    animal_date_of_birth, age_precision = get_animal_date_of_birth(description, created_time_stamp)
    field_value_info = get_field_value_info(description)
    tag = get_animal_tag(description)
    vals = (tag, animal_date_of_birth, age_precision, field_value_info)
    res = {key: val for key, val in zip(DESCR_DATA_KEYS, vals) if val}
    return res
