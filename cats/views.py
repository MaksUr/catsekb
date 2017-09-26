from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from cats.models import Animal, Group


class AnimalListView(ListView):
    # template animal_list
    model = Animal
    # TODO: parse get parameters and get animals

    def get_queryset(self):
        req = self.request.GET.dict()
        query = dict()
        if req.get('name'):
            query['name__istartswith'] = req['name']
        if req.get('sex'):
            query['sex'] = req['sex']
        # TODO: добавить свойства
        query['show'] = True

        if req.get('group_id'):
            res = Animal.objects.filter(**query).get_animals_by_group_id(req['group_id'])
        elif req.get('group'):
            res = Animal.objects.filter(**query).get_animals_by_group_name(req['group'])
        else:
            res = Animal.objects.filter(**query)
        return res


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal
    animal_paginate_by = 1

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        animal = kwargs['object']
        group_name = self.get_group_name()
        if group_name is not None:
            # TODO: check
            animals = Animal.objects.get_animals_by_group_name(group_name)
            context['page'] = self.get_animal_page(animals, animal)
        return context

    def get_group_name(self):
        res = self.kwargs.get('group_pk')
        return res

    @staticmethod
    def get_animal_page(animals, animal):
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
            return page


class GroupListView(ListView):
    # template group_list
    model = Group


class GroupDetailView(ListView):
    # template group_detail
    model = Group

    def __init__(self, **kwargs):
        ListView.__init__(self, **kwargs)
    # TODO: implement
    # def get_context_data(self, **kwargs):
    #     context = ListView.get_context_data(self, **kwargs)
    #     group_id = self.kwargs['pk']
    #     animals = Animal.objects.get_animals_by_group_id(group_id).filter(show=True)
    #     context['animals'] = animals
    #     return context

    # def get_q


def index_view(request):
    return render(request, 'cats/index.html', {})



# #####################################################
# def animal_view(request, animal_id, group_id=None):  # TODO: rename
#     """
#
#     :type request: HttpResponse
#     :type animal_id: str
#     :type group_id: str
#     """
#     animal_id = check_and_get_int_id(animal_id)
#     animal = get_animal_by_id(animal_id)
#
#     if group_id is None:
#         page = None
#     else:
#         group_name, group_id, animals_id_list,  = get_animals_from_group(group_id)
#         animals_id_list = [i[0] for i in animals_id_list]
#         try:
#             i = animals_id_list.index(animal_id) + 1
#         except ValueError:
#             # TODO: id in current group does not exist
#             raise Exception("В данной группе нет животного с таким айди")
#         paginator = Paginator(animals_id_list, 1)
#         page = paginator.page(i)
#
#     return render(request, 'cats/animal.html', {'group': group_id, 'animal': animal, 'page': page})
#
