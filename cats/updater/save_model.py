from django.core.exceptions import ObjectDoesNotExist

from cats.models import Animal, AnimalImage


def save_animal(**kwargs):
    try:
        a = Animal(**kwargs)
    except TypeError:
        return None
    a.save()
    return a


def save_image(**kwargs):
    try:
        i = AnimalImage(**kwargs)
    except TypeError:
        return None
    i.save()
    return i


def update_animal(animal, **kwargs):
    for k in kwargs:
        animal.__setattr__(k, kwargs[k])
    try:
        animal.save(update_fields=kwargs.keys())
    except ValueError:
        return None
    return animal


def get_or_create_animal(**kwargs):
    try:
        res = Animal.objects.get(**kwargs)
    except (Animal.MultipleObjectsReturned,):
        res = Animal.objects.filter(**kwargs).first()
    except ObjectDoesNotExist:
        res = save_animal(**kwargs)
    return res
