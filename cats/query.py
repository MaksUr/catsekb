from django.db.models import QuerySet


class AnimalQuerySet(QuerySet):

    def get_animals_by_group_id(self, group):
        """

        :type group: str
        """
        if group == 'all' or group is None:
            return self.all()
        res = self.filter(group__pk=group)
        return res

    def get_animals_by_group_name(self, group=None):
        """

        :type group: str
        """
        if group == 'all' or group is None:
            return self.all()
        else:
            res = self.filter(group__name=group)
            return res


