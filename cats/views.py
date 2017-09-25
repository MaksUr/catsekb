from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cats.models import Animal, Group


class AnimalListView(ListView):
    # template animal_list
    model = Animal


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal


class GroupListView(ListView):
    # template group_list
    model = Group


class GroupDetailView(DetailView):
    # template group_detail
    model = Group
    # TODO: add pagination


def index_view(request):
    return render(request, 'cats/index.html', {})
