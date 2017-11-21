import re

from cats.constants import ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_DEAD, ANIMAL_LOCATION_STATUS_SHELTER, \
    ANIMAL_SEX_MALE, ANIMAL_SEX_FEMALE

CHANGE_NAME_PATTERN = re.compile(r"(^[\W_]*)|([\W_]*$)")

STATUS_HOME = ANIMAL_LOCATION_STATUS_HOME
STATUS_DIE = ANIMAL_LOCATION_STATUS_DEAD
STATUS_SHELTER = ANIMAL_LOCATION_STATUS_SHELTER


LABEL = 'label'
PATTERN = 'pattern'

MAPPING = {
    STATUS_HOME: {
        LABEL: 'ПРИСТРОЕН',
        PATTERN: re.compile(
            r"([ -]+)?(_)?(!)?ПРИСТРОЕН([АЫ])?(_)?(!)?( +)?",
            flags=re.IGNORECASE
        ),
    },
    STATUS_DIE: {
        LABEL: 'НА РАДУГЕ',
        PATTERN: re.compile(
            r"_?НА РАДУГЕ_?([ ]+)?",
            flags=re.IGNORECASE
        )
    },
    STATUS_SHELTER: {
        LABEL: 'В ПРИЮТЕ',
        PATTERN: None
    },
}


def change_name(s, pattern, replacing):
    m = re.sub(pattern, replacing, s)
    return m


def replace_str_end_at_empty(s):
    return change_name(s, CHANGE_NAME_PATTERN, '')


def check_name_status(name, status):
    res = None
    pattern = MAPPING[status][PATTERN]
    if pattern is None:
        res = name
    else:
        m = re.search(pattern, name)
        if m is not None:
            match = m.group()
            r = name.replace(match, "")
            res = r or None

    if res is not None:
        res = replace_str_end_at_empty(res)
    return res


def analyse_animal_name(name):
    r = check_name_status(name, STATUS_HOME)
    if r is not None:
        return STATUS_HOME, r
    else:
        r = check_name_status(name, STATUS_DIE)
        if r is not None:
            return STATUS_DIE, r
        else:
            r = check_name_status(name, STATUS_SHELTER)
            if r is None:
                return None, None
            return STATUS_SHELTER, r


PATTERN_SEX_M = re.compile(r"ПРИСТРОЕН(?!А)", flags=re.IGNORECASE)
PATTERN_SEX_F = re.compile(r"ПРИСТРОЕНА", flags=re.IGNORECASE)


def get_sex(title):
    if re.search(PATTERN_SEX_M, title) is not None:
        return ANIMAL_SEX_MALE
    elif re.search(PATTERN_SEX_F, title) is not None:
        return ANIMAL_SEX_FEMALE
    else:
        return None
