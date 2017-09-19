from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cats.models import Animal, Group


def index(request):
    animals = Animal.objects.filter(show=True)
    groups = Group.objects.filter(show=True)
    return render(request, 'cats/index.html', locals())


def animal(request, animal_id, group_id=None):
    next_animal_id = 5  # TODO: set next
    last_animal_id = 3  # TODO: set next
    animal_by_id = Animal.objects.get(id=animal_id, show=True)  # TODO: check does not exist
    return render(
        request,
        'cats/animal.html',
        {
            'animal': animal_by_id, 'next': next_animal_id, 'last': last_animal_id
        }
    )


def group(request, group_id):
    group = Group.objects.get(id=group_id, show=True)  # TODO: check does not exist
    name = group.name
    id = group.id
    animals = group.animal_set.filter(show=True)
    return render(request, 'cats/group.html', {'group': animals, 'name': name, 'id': id})
