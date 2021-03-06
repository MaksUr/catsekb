from django.db.models import QuerySet

from cats.cats_constants import ANIMAL_GROUP, ANIMAL_NAME, AGE_DISTANCE, \
    ANIMAL_DATE_OF_BIRTH, GROUP_NAME, \
    ANIMAL_LOCATION_STATUS, GROUP_ID, ANIMAL_SEX, SHELTER_DISTANCE, ANIMAL_SHELTER_DATE
from catsekb.constants import DJ_PK, NO_CHOICE_VALUE
from cats.time import get_age_from_string, get_date_from_age

TEMPLATE = '{arg1}__{arg2}'


NAME__ISTARTSWITH = TEMPLATE.format(arg1=ANIMAL_NAME, arg2='istartswith')
GROUP__NAME = TEMPLATE.format(arg1=ANIMAL_GROUP, arg2=GROUP_NAME)
GROUP__PK = TEMPLATE.format(arg1=ANIMAL_GROUP, arg2=DJ_PK)
LOCATION_GROUP_MAPPING = (
        'H',
        'S',
        'D',
)

ANIMAL_QUERY_KEYS = (
    GROUP_ID,
    ANIMAL_GROUP,
    ANIMAL_NAME,
    AGE_DISTANCE,
    SHELTER_DISTANCE,
    ANIMAL_LOCATION_STATUS,
    ANIMAL_SEX,
    'project',
)


def update_distance_kwargs(kwargs, kwargs_key, field_name):
    try:
        start_distance, end_distance = kwargs[kwargs_key].split('_')
    except ValueError:
        pass
    else:
        if start_distance:
            age_start = get_age_from_string(start_distance)
            if age_start:
                start_date = get_date_from_age(**age_start)
                kwargs[TEMPLATE.format(arg1=field_name, arg2='lte')] = start_date

        if end_distance:
            age_end = get_age_from_string(end_distance)
            if age_end:
                end_date = get_date_from_age(**age_end)
                kwargs[TEMPLATE.format(arg1=field_name, arg2='gte')] = end_date
    finally:
        del kwargs[kwargs_key]


class AnimalQuerySet(QuerySet):
    def filter(self, *args, **kwargs):
        kwargs = {key: kwargs[key] for key in kwargs if kwargs[key] != NO_CHOICE_VALUE}
        if kwargs.get(GROUP_ID) is not None and (kwargs[GROUP_ID] != NO_CHOICE_VALUE):
            if kwargs[GROUP_ID] in LOCATION_GROUP_MAPPING:
                kwargs[ANIMAL_LOCATION_STATUS] = kwargs[GROUP_ID]
            elif kwargs[GROUP_ID] != 'all':
                kwargs[GROUP__PK] = kwargs[GROUP_ID]
            del kwargs[GROUP_ID]

        if kwargs.get(ANIMAL_GROUP) is not None:
            if kwargs[ANIMAL_GROUP] != 'Все котики':
                kwargs[GROUP__NAME] = kwargs[ANIMAL_GROUP]
            del kwargs[ANIMAL_GROUP]

        if kwargs.get(ANIMAL_NAME) is not None:
            kwargs[NAME__ISTARTSWITH] = kwargs[ANIMAL_NAME]
            del kwargs[ANIMAL_NAME]

        if kwargs.get(AGE_DISTANCE) is not None:
            update_distance_kwargs(kwargs=kwargs, kwargs_key=AGE_DISTANCE, field_name=ANIMAL_DATE_OF_BIRTH)
        if kwargs.get(SHELTER_DISTANCE) is not None:
            update_distance_kwargs(kwargs=kwargs, kwargs_key=SHELTER_DISTANCE, field_name=ANIMAL_SHELTER_DATE)
            kwargs[ANIMAL_LOCATION_STATUS] = 'S'

        res = QuerySet.filter(self, *args, **kwargs)
        return res
