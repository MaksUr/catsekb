from django.core.exceptions import FieldError
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView

from cats.constants import FILTER_LABEL, GROUP_ALL_ANIMALS_NAME, ANIMAL_CREATED, ANIMAL_SHOW, DJ_PK, DJ_PAGE, DJ_OBJECT, \
    GROUP_SHOW
from cats.forms import FilterForm
from cats.models import Animal, Group


def get_group(group_id, show_permission=False):
    if group_id == GROUP_ALL_ANIMALS_NAME:
        return Group.get_group_with_all_animals()
    else:
        query = dict()
        query['id'] = group_id
        if show_permission is False:
            query['show'] = True
        res = get_object_or_404(Group, **query)
        return res


def get_animals_from_query(query, show_permission=False):
    """

    :type show_permission: bool
    :type query: dict
    """
    if show_permission is False:
        query[ANIMAL_SHOW] = True
    try:
        res = Animal.objects.filter(**query).order_by(ANIMAL_CREATED)
    except FieldError:
        raise Http404("Запрос неверный")
    return res


def get_groups_from_query(query, show_permission=False):
    """

    :type show_permission: bool
    :type query: dict
    """
    if show_permission is False:
        query[GROUP_SHOW] = True
    try:
        res = Group.objects.filter(**query)
    except FieldError:
        raise Http404("Запрос неверный")
    return res


def get_filter_string(query):
    """

    :type query: QueryDict
    """
    if query:
        return '?'+query.urlencode()
    else:
        return ''


# TODO: доступен только админам или из фильтра с контролем параметров
class AnimalListView(ListView):
    # template animal_list
    model = Animal

    def get_queryset(self):
        show_permission = self.request.user.is_authenticated()
        query = self.request.GET.dict()
        res = get_animals_from_query(query, show_permission=show_permission)
        return res

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['filter_string'] = get_filter_string(self.request.GET)
        context['filter_label'] = FILTER_LABEL
        return context


class AnimalDetailView(DetailView):
    # TODO: if show=False check admin login
    # template animal_detail
    model = Animal
    animal_paginate_by = 1

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        animal = kwargs[DJ_OBJECT]
        show_permission = self.request.user.is_authenticated()
        if show_permission is False and animal.show is False:
            raise Http404("Нет прав для просмотра этой страницы")
        animals_query = self.get_animals_query()
        if animals_query:
            animals = get_animals_from_query(animals_query, show_permission=show_permission)
            context[DJ_PAGE] = self.get_animal_page(animals, animal)
        return context

    def get_animals_query(self):
        res = self.request.GET.dict()
        return res

    @staticmethod
    def get_animal_page(animals, animal):
        if animal not in animals:
            # TODO: redirect without group
            return None
            # raise Http404('Анимал отсутствует в данной группе')
        else:
            animals_id_list = [i.id for i in animals]
            try:
                page_number = animals_id_list.index(animal.id) + 1
            except ValueError:
                return None
            paginator = Paginator(animals_id_list, 1)
            page = paginator.page(page_number)
            return page


class GroupListView(ListView):
    # template group_list
    model = Group

    def get_queryset(self):
        show_permission = self.request.user.is_authenticated()
        group_list = get_groups_from_query(dict(), show_permission=show_permission)
        return group_list


class GroupDetailView(ListView):
    # template group_detail
    model = Group
    template_name = 'cats/group_detail.html'

    def get_queryset(self):
        show_permission = self.request.user.is_authenticated()
        return Animal.objects.filter(group_id=self.kwargs[DJ_PK], show=show_permission)

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        group_id = self.kwargs[DJ_PK]
        group = get_group(group_id=group_id, show_permission=show_permission)
        context[DJ_OBJECT] = group
        return context


def index_view(request):
    show_permission = request.user.is_authenticated()
    all_animals_group = get_group(GROUP_ALL_ANIMALS_NAME, show_permission=show_permission)
    all_animals_list = get_animals_from_query(dict(), show_permission=show_permission)
    group_list = get_groups_from_query(dict(), show_permission=show_permission)
    filter_label = FILTER_LABEL
    return render(request, 'cats/index.html', locals())  # TODO: delete locals


class FilterView(FormView):
    template_name = 'cats/animal_filter.html'
    form_class = FilterForm

    def get_context_data(self, **kwargs):
        context = FormView.get_context_data(self, **kwargs)
        if self.request.GET.dict():
            show_permission = self.request.user.is_authenticated()
            query = self.request.GET
            context['animal_list'] = get_animals_from_query(query.dict(), show_permission=show_permission)
            context['filter_string'] = get_filter_string(query)
        return context

    def get_form_kwargs(self):
        res = FormView.get_form_kwargs(self)
        res['data'] = self.request.GET.dict()
        return res




