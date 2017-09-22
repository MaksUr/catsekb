from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from cats.models import Animal, Group


def check_and_get_int_id(str_id):
    """

    :type str_id: str
    """
    if str_id.isdigit():
        return int(str_id)
    else:
        raise ValueError("Id must be integer.")


def get_animal_by_id(animal_id):
    try:
        animal = Animal.objects.get(show=True, id=animal_id)
    except Exception:   # TODO: 404
        raise Exception("Животного с данным айди и show=True нету в базе данных")
    return animal


def get_animals_from_group(group_id):
    """

    :type group_id: str
    """
    if group_id == Animal.ALL_ANIMALS_KEY:
        group_name = Animal.ALL_ANIMALS
        animals_id = Animal.objects.filter(show=True).values_list('id', 'name')
    else:
        try:
            group_id = check_and_get_int_id(group_id)
        except ValueError:
            # TODO: 404
            raise Exception("Группа задана неккоректно, должна быть int")
        try:
            group_animals = Group.objects.get(id=group_id, show=True)
        except ObjectDoesNotExist:
            # TODO: 404
            raise Exception("Группы с данным айди и show=True нету в базе данных")
        group_name = group_animals.name
        animals_id = group_animals.animal_set.filter(show=True).values_list('id', 'name')

    return group_name, group_id, list(animals_id)


def index(request):  # TODO: rename
    groups = Group.objects.filter(show=True)
    name, group_id, animals = get_animals_from_group(Animal.ALL_ANIMALS_KEY)
    return render(request, 'cats/index.html', {'group': animals, 'name': name, 'id': group_id, 'groups': groups})


def animal(request, animal_id, group_id=None):  # TODO: rename
    """

    :type request: HttpResponse
    :type animal_id: str
    :type group_id: str
    """
    animal_id = check_and_get_int_id(animal_id)
    animal = get_animal_by_id(animal_id)

    if group_id is None:
        page = None
    else:
        group_name, group_id, animals_id_list,  = get_animals_from_group(group_id)
        animals_id_list = [i[0] for i in animals_id_list]
        try:
            i = animals_id_list.index(animal_id) + 1
        except ValueError:
            # TODO: id in current group does not exist
            raise Exception("В данной группе нет животного с таким айди")
        paginator = Paginator(animals_id_list, 1)
        page = paginator.page(i)

    return render(request, 'cats/animal.html', {'group': group_id, 'animal': animal, 'page': page})


def group(request, group_id):  # TODO: rename
    name, group_id, animals = get_animals_from_group(group_id)
    return render(request, 'cats/group.html', {'group': animals, 'name': name, 'id': group_id})
