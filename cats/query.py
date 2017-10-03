from django.db.models import QuerySet

from cats.constants import GROUP_ALL_ANIMALS_KEY_NAME
from cats.time import get_age_from_string, get_date_from_age

NAME = 'name'

NAME__ISTARTSWITH = 'name__istartswith'

GROUP__NAME = 'group__name'

GROUP = 'group'

GROUP__PK = 'group__pk'

ALL = 'all'

GROUP_ID = 'group_id'

AGE_DISTANCE = 'age_distance'


class AnimalQuerySet(QuerySet):

    def filter_animals(self, **kwargs):
        if kwargs.get(GROUP_ID) is not None:
            if kwargs[GROUP_ID] != ALL:
                kwargs[GROUP__PK] = kwargs[GROUP_ID]
            del kwargs[GROUP_ID]

        if kwargs.get(GROUP) is not None:
            if kwargs[GROUP] != GROUP_ALL_ANIMALS_KEY_NAME:
                kwargs[GROUP__NAME] = kwargs[GROUP]
            del kwargs[GROUP]

        if kwargs.get(NAME) is not None:
            kwargs[NAME__ISTARTSWITH] = kwargs[NAME]
            del kwargs[NAME]

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
                        kwargs['date_of_birth__lte'] = start_date

                if end_distance:
                    age_end = get_age_from_string(end_distance)
                    if age_end:
                        end_date = get_date_from_age(**age_end)
                        kwargs['date_of_birth__gte'] = end_date
            finally:
                del kwargs[AGE_DISTANCE]
        return self.filter(**kwargs)
