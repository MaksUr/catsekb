from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from cats.models import Animal, Group


def get_group(group_name):
    if group_name == 'all':
        return Group.get_group_with_all_animals()
    else:
        res = get_object_or_404(Group, id=group_name, show=True)
        return res


# TODO: доступен только админам или из фильтра с контролем параметров
class AnimalListView(ListView):
    # template animal_list
    model = Animal

    def __init__(self, **kwargs):
        ListView.__init__(self, **kwargs)
        self.context = dict()

    def get_queryset(self):
        query = self.request.GET.dict()
        query['show'] = True
        res = Animal.objects.filter_animals(**query)
        if self.kwargs.get('group_pk') is not None:
            res = res.filter_animals(group_id=self.kwargs['group_pk'])
            self.context['group_id'] = self.kwargs['group_pk']
        return res

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update(self.context)
        return context


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal
    animal_paginate_by = 1

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        animal = kwargs['object']
        group_id = self.get_group_id()
        if group_id is not None:
            # TODO: check
            animals = Animal.objects.filter_animals(group_id=group_id)
            context['page'] = self.get_animal_page(animals, animal, group_id)
        return context

    def get_group_id(self):
        res = self.kwargs.get('group_pk')
        return res

    @staticmethod
    def get_animal_page(animals, animal, group_id):
        if animal not in animals:
            # TODO: check
            raise Http404('Анимал отсутствует в данной группе')
            # TODO: redirect without group
        else:
            animals_id_list = [i.id for i in animals]
            try:
                page_number = animals_id_list.index(animal.id) + 1
            except ValueError:
                # TODO: check
                return None
            paginator = Paginator(animals_id_list, 1)
            page = paginator.page(page_number)
            page.group_id = group_id
            return page


class GroupListView(ListView):
    # template group_list
    model = Group


class GroupDetailView(ListView):
    # template group_detail
    model = Group
    template_name = 'cats/group_detail.html'

    def get_queryset(self):
        return Animal.objects.filter_animals(group_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        group_name = self.kwargs['pk']
        group = get_group(group_name)
        context['object'] = group
        return context


def index_view(request):
    all_animals_group = get_group('all')
    # TODO: edit
    all_animals_list = Animal.objects.filter(show=True)
    group_list = Group.objects.filter(show=True)
    return render(request, 'cats/index.html', locals())
