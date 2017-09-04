from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cats.models import Animal


def index(request):
    animals = Animal.objects.filter(show=True)
    return render(request, 'cats/index.html', {'animals': animals})


def animal(request, animal_id):
    animal_by_id = Animal.objects.get(id=animal_id)
    return render(request, 'cats/animal.html', {'animal': animal_by_id})
