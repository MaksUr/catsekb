from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cats.cats_constants import ANIMAL_CREATED, DJ_PK, DJ_PAGE, DJ_OBJECT, \
    ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_SHELTER, ANIMAL_LOCATION_STATUS, \
    CAPTION_ANIMAL_LIST_DEFAULT, GROUP_ID, ANIMAL_LOCATION_STATUS_DEAD, INDEX, ANIMALS, \
    GROUP_INSTANCE_SHELTER_NAME, SHOW_FILTER_KEY, PER_PAGE, PER_PAGE_ALL, PAGE
from cats.forms import FilterForm
from cats.models import Animal, Group
from cats.query import ANIMAL_QUERY_KEYS
from catsekb.view_functions import get_objects_from_query, get_base_context, get_group

GALLERY_DEFAULT_ITEMS_COUNT = 9


def filter_animals_query(query):
    res = {key: query[key] for key in query if key in ANIMAL_QUERY_KEYS}
    return res


def get_animals_from_query(query, show_permission=False):
    """

    :rtype: QueryDict
    :type show_permission: bool
    :type query: dict
    """
    query = filter_animals_query(query)
    res = get_objects_from_query(
        model_cls=Animal, query=query, show_permission=show_permission, order_by=ANIMAL_CREATED
    )
    return res


class AnimalListView(ListView, FormMixin):
    paginate_by = GALLERY_DEFAULT_ITEMS_COUNT
    model = Animal
    form_class = FilterForm
    template_name = 'cats/animal_list.html'
    caption = CAPTION_ANIMAL_LIST_DEFAULT
    description = ''
    show_filter = False

    def get_queryset(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        query = self.request.GET.dict()
        query.update(kwargs)
        self.show_filter = query.pop(SHOW_FILTER_KEY, False)
        if self.show_filter and not(set(query) & set(ANIMAL_QUERY_KEYS)):
            res = Animal.objects.none()
        else:
            res = get_animals_from_query(query, show_permission=show_permission)
        return res

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS))
        context['filter_string'] = self.get_filter_string()
        context['caption'] = self.caption
        if self.show_filter:
            u = FormMixin.get_context_data(self, **kwargs)
            context.update(u)
            context['description'] = 'Найдено {count} котиков'.format(count=len(self.object_list))
        else:
            context['description'] = self.description
            del context['form']
        return context

    def get_filter_string(self, update_dict=None):
        query = self.request.GET.copy()
        query._mutable = True
        if update_dict:
            query.update(update_dict)
        if self.show_filter:
            query[SHOW_FILTER_KEY] = 1
        if query:
            return '?' + query.urlencode()
        else:
            return ''

    def get_paginate_by(self, queryset):
        if self.request.GET.get(PER_PAGE) is not None:
            per_page_param = self.request.GET.get(PER_PAGE)
            if per_page_param == PER_PAGE_ALL:
                self.kwargs[PAGE] = 1
                return len(queryset)
            else:
                try:
                    return int(per_page_param)
                except ValueError:
                    return self.paginate_by
        else:
            return self.paginate_by

    def get_form_kwargs(self):
        res = super(AnimalListView, self).get_form_kwargs()
        res['data'] = self.request.GET.dict()
        return res


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS))
        animal = kwargs[DJ_OBJECT]
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
            return None
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
        group_list = get_objects_from_query(model_cls=Group, query=dict(), show_permission=show_permission)
        return group_list

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=self.request.user.is_authenticated(), active_menu=ANIMALS))
        return context


class GroupDetailView(AnimalListView):

    def get_queryset(self):
        res = super(GroupDetailView, self).get_queryset(group_id=self.kwargs[DJ_PK])
        return res

    def get_context_data(self, **kwargs):
        group_id = self.kwargs[DJ_PK]
        group = get_group(group_id=group_id, show_permission=self.request.user.is_authenticated())
        self.caption = group.name
        self.description = group.description
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        return context

    def get_filter_string(self, update_dict=None):
        upd = {GROUP_ID: self.kwargs[DJ_PK]}
        res = super(GroupDetailView, self).get_filter_string(update_dict=upd)
        return res


def index_view(request):
    show_permission = request.user.is_authenticated()
    context = get_base_context(show_permission=show_permission, active_menu=INDEX)
    query = {ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_SHELTER}
    shelter_animals = get_animals_from_query(
        query=query, show_permission=show_permission
    ).order_by('?')
    context['shelter_animals'] = shelter_animals[:GALLERY_DEFAULT_ITEMS_COUNT]
    context['shelter_caption'] = GROUP_INSTANCE_SHELTER_NAME
    context['shelter_animals_count'] = shelter_animals.count()
    context['home_animals_count'] = get_animals_from_query(
        query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_HOME}, show_permission=True
    ).count()  # TODO: need correct number
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    if show_permission is True:
        context['dying_animals_count'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_DEAD}, show_permission=True
        ).count()
    return render(request, 'cats/index.html', context)
