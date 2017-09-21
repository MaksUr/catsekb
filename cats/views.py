from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cats.models import Animal, Group

######################################


def index_test(request):
    animal_list = Animal.objects.filter(show=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(animal_list, 2)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    return render(request, 'cats/index_test.html', {'animals': animals})
######################################


def index(request):
    animals = Animal.objects.filter(show=True)
    groups = Group.objects.filter(show=True)
    all_animals_group_name = Animal.ALL_ANIMALS
    all_animals_group_key = Animal.ALL_ANIMALS_KEY
    return render(request, 'cats/index.html', locals())


def animal(request, group_id=None):
    """

    :type group_id: str
    """
    animal_id = request.GET.get('page', Animal.object)
    query = {'id': animal_id, 'show': True}
    if group_id == Animal.ALL_ANIMALS_KEY:
        pass
    elif group_id.isdigit():
        animal_id = int(group_id)
        # query['group'] = Group.objects.get(show=True, id=animal_id)


    # params = dict()
    # query = {'id': animal_id, 'show': True}
    # if group_id == 'all':
    #     params['group'] = 'all'
    # elif isinstance(group_id, int):
    #     params['group'] = group_id
    #     query['group'] = Group.objects.get(show=True, id=group_id)  # TODO: check does not exist
    #
    # animal_by_id = Animal.objects.get(**query)  # TODO: check does not exist
    # if group_id is not None:
    #     # next_animal_id = animal_by_id.get_next_by_id().id  # TODO: set next
    #     # last_animal_id = animal_by_id.get_previous_by_id().id  # TODO: set next
    #     next_animal_id = 3
    #     last_animal_id = 5
    #     params['next'] = next_animal_id
    #     params['last'] = last_animal_id
    # params['animal'] = animal_by_id
    return render(request, 'cats/animal.html', params)


def group(request, group_id):  # TODO: rename
    if group_id == 'all':
        animals = Animal.objects.filter(show=True)
        name = Animal.ALL_ANIMALS
        id = group_id
    else:
        group = Group.objects.get(id=group_id, show=True)  # TODO: check does not exist
        name = group.name
        id = group.id
        animals = group.animal_set.filter(show=True)
    return render(request, 'cats/group.html', {'group': animals, 'name': name, 'id': id})
