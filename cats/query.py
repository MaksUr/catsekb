from django.db.models import QuerySet

from cats.constants import GROUP_ALL_ANIMALS_KEY_NAME, ANIMAL_GROUP, ANIMAL_NAME, GROUP_ALL_ANIMALS_NAME, AGE_DISTANCE, \
    ANIMAL_DATE_OF_BIRTH, GROUP_NAME, DJ_PK
from cats.time import get_age_from_string, get_date_from_age

TEMPLATE = '{arg1}__{arg2}'


DATE_OF_BIRTH__GTE = TEMPLATE.format(arg1=ANIMAL_DATE_OF_BIRTH, arg2='gte')
DATE_OF_BIRTH__LTE = TEMPLATE.format(arg1=ANIMAL_DATE_OF_BIRTH, arg2='lte')
NAME__ISTARTSWITH = TEMPLATE.format(arg1=ANIMAL_NAME, arg2='istartswith')
GROUP__NAME = TEMPLATE.format(arg1=ANIMAL_GROUP, arg2=GROUP_NAME)
GROUP__PK = TEMPLATE.format(arg1=ANIMAL_GROUP, arg2=DJ_PK)
GROUP_ID = 'group_id'


class AnimalQuerySet(QuerySet):

    def filter_animals(self, **kwargs):
        if kwargs.get(GROUP_ID) is not None:
            if kwargs[GROUP_ID] != GROUP_ALL_ANIMALS_NAME:
                kwargs[GROUP__PK] = kwargs[GROUP_ID]
            del kwargs[GROUP_ID]

        if kwargs.get(ANIMAL_GROUP) is not None:
            if kwargs[ANIMAL_GROUP] != GROUP_ALL_ANIMALS_KEY_NAME:
                kwargs[GROUP__NAME] = kwargs[ANIMAL_GROUP]
            del kwargs[ANIMAL_GROUP]

        if kwargs.get(ANIMAL_NAME) is not None:
            kwargs[NAME__ISTARTSWITH] = kwargs[ANIMAL_NAME]
            del kwargs[ANIMAL_NAME]

        if kwargs.get(AGE_DISTANCE) is not None:
            try:
                start_distance, end_distance = kwargs[AGE_DISTANCE].split('_')
            except ValueError:
                pass
            else:
                if start_distance:
                    age_start = get_age_from_string(start_distance)
                    if age_start:
                        start_date = get_date_from_age(**age_start)
                        kwargs[DATE_OF_BIRTH__LTE] = start_date

                if end_distance:
                    age_end = get_age_from_string(end_distance)
                    if age_end:
                        end_date = get_date_from_age(**age_end)
                        kwargs[DATE_OF_BIRTH__GTE] = end_date
            finally:
                del kwargs[AGE_DISTANCE]
        return self.filter(**kwargs)
