from django.db.models import QuerySet

from cats.constants import GROUP_ALL_ANIMALS_KEY_NAME

NAME = 'name'

NAME__ISTARTSWITH = 'name__istartswith'

GROUP__NAME = 'group__name'

GROUP = 'group'

GROUP__PK = 'group__pk'

ALL = 'all'

GROUP_ID = 'group_id'


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
        return self.filter(**kwargs)
