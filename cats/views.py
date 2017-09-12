from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cats.models import Animal, Group


def index(request):
    animals = Animal.objects.filter(show=True)
    groups = Group.objects.filter(show=True)
    return render(request, 'cats/index.html', locals())


def animal(request, animal_id):
    animal_by_id = Animal.objects.get(id=animal_id)
    return render(request, 'cats/animal.html', {'animal': animal_by_id})


def group(request, group_id):
    group_by_id = Group.objects.get(id=group_id).animal_set.filter(show=True)
    return render(request, 'cats/group.html', {'group': group_by_id})