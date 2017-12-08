from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cats.cats_constants import ANIMAL_CREATED, ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_SHELTER, \
    ANIMAL_LOCATION_STATUS, \
    GROUP_ID, ANIMAL_LOCATION_STATUS_DEAD, GROUP_INSTANCE_SHELTER_NAME, GROUP_INSTANCE_HOME_NAME, \
    GROUP_INSTANCE_DEAD_NAME, GROUP_INSTANCE_SHELTER_ID, GROUP_INSTANCE_HOME_ID, GROUP_INSTANCE_DEAD_ID, \
    GROUP_ANIMALS_PREVIEW_COUNT, ANIMAL_LOCATION_STATUS_CHOICES_D, GROUP_MAPPING
from catsekb.constants import CAPTION_ANIMAL_LIST_DEFAULT, INDEX, ANIMALS, GET_PAR_KEY_PAGE, GET_PAR_KEY_PER_PAGE, \
    GET_PAR_VAL_PAGE, \
    GET_PAR_KEY_FILTER, DJ_PK, DJ_PAGE, DJ_OBJECT, URL_NAME_GROUP, NAME, DESCRIPTION, URL_NAME_GROUPS_TITLE, \
    URL_NAME_INDEX_TITLE
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

    def set_description_and_caption(self, query):
        if len(query) == 1 and ANIMAL_LOCATION_STATUS in query:
            try:
                self.caption = GROUP_MAPPING[query[ANIMAL_LOCATION_STATUS]][NAME]
                self.description = GROUP_MAPPING[query[ANIMAL_LOCATION_STATUS]][DESCRIPTION]
            except KeyError:
                pass

    def get_queryset(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        query = self.request.GET.dict()
        query.update(kwargs)
        self.show_filter = query.pop(GET_PAR_KEY_FILTER, False)
        self.set_description_and_caption(query)
        if self.show_filter and not(set(query) & set(ANIMAL_QUERY_KEYS)):
            res = Animal.objects.none()
        else:
            res = get_animals_from_query(query, show_permission=show_permission)
        return res

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context['filter_string'] = self.get_filter_string()
        context['caption'] = self.caption
        context['description'] = self.description
        if self.show_filter:
            u = FormMixin.get_context_data(self, **kwargs)
            context.update(u)
            context['description'] = 'Найдено {count} котиков'.format(count=len(self.object_list))
        else:
            context['description'] = self.description
            del context['form']
        extra_title = context['caption'] + ' ' + context['description']
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS, extra_title=extra_title))
        return context

    def get_filter_string(self, update_dict=None):
        query = self.request.GET.copy()
        query._mutable = True
        if update_dict:
            query.update(update_dict)
        if self.show_filter:
            query[GET_PAR_KEY_FILTER] = 1
        if query:
            return '?' + query.urlencode()
        else:
            return ''

    def get_paginate_by(self, queryset):
        per_page = self.request.GET.get(GET_PAR_KEY_PER_PAGE)
        if per_page is not None:
            if per_page == GET_PAR_VAL_PAGE:
                self.kwargs[GET_PAR_KEY_PAGE] = 1
                return len(queryset)
            else:
                try:
                    return int(per_page)
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
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS, extra_title=self.object.__str__()))
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
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS, extra_title=URL_NAME_GROUPS_TITLE))

        context['shelter_caption'] = GROUP_INSTANCE_SHELTER_NAME
        context['shelter_url'] = reverse(URL_NAME_GROUP, kwargs={DJ_PK: GROUP_INSTANCE_SHELTER_ID})
        context['shelter_animals'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_SHELTER},
            show_permission=show_permission
        ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        context['home_caption'] = GROUP_INSTANCE_HOME_NAME
        context['home_url'] = reverse(URL_NAME_GROUP, kwargs={DJ_PK: GROUP_INSTANCE_HOME_ID})
        context['home_animals'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_HOME},
            show_permission=show_permission
        ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        if show_permission is True:
            context['dying_caption'] = GROUP_INSTANCE_DEAD_NAME
            context['dying_url'] = reverse(URL_NAME_GROUP, kwargs={DJ_PK: GROUP_INSTANCE_DEAD_ID})
            context['dying_animals'] = get_animals_from_query(
                query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_DEAD},
                show_permission=show_permission
            ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        context['groups'] = get_objects_from_query(model_cls=Group, query=dict(), show_permission=show_permission)
        return context


class GroupDetailView(AnimalListView):

    def set_description_and_caption(self, query):
        group = get_group(group_id=self.kwargs[DJ_PK], show_permission=self.request.user.is_authenticated())
        self.description = group.description
        self.caption = group.name

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
    context = get_base_context(show_permission=show_permission, active_menu=INDEX, extra_title=URL_NAME_INDEX_TITLE)
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
