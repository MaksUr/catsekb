from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from articles.article_constants import ARTICLES_DEFAULT, ARTICLE_FIND_CAT_ID, URL_NAME_FIND_CAT
from articles.models import Subject
from cats.constants import GROUP_INSTANCE_ALL_ID, ANIMAL_CREATED, ANIMAL_SHOW, DJ_PK, DJ_PAGE, DJ_OBJECT, \
    GROUP_SHOW, ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_SHELTER, GROUP_INSTANCE_ALL_NAME, \
    ANIMAL_LOCATION_STATUS, \
    CAPTION_ANIMAL_LIST_DEFAULT, GROUP_ID, GROUP_INSTANCE_ALL_DESCR, GROUP_INSTANCE_HOME_DESCR, \
    GROUP_INSTANCE_SHELTER_DESCR, ANIMAL_LOCATION_STATUS_DEAD, GROUP_INSTANCE_DEAD_DESCR, INDEX, ANIMALS, \
    GROUP_INSTANCE_SHELTER_ID, \
    GROUP_INSTANCE_HOME_ID, GROUP_INSTANCE_DEAD_ID, GROUP_INSTANCE_SHELTER_NAME, GROUP_INSTANCE_HOME_NAME, \
    GROUP_INSTANCE_DEAD_NAME, URL_NAME_ANIMALS
from cats.forms import FilterForm
from cats.models import Animal, Group
from cats.query import ANIMAL_QUERY_KEYS

GROUP_MAPPING = {
    GROUP_INSTANCE_ALL_ID: {
        'name': GROUP_INSTANCE_ALL_NAME,
        'description': GROUP_INSTANCE_ALL_DESCR,
    },
    GROUP_INSTANCE_HOME_ID: {
        'name': GROUP_INSTANCE_HOME_NAME,
        'description': GROUP_INSTANCE_HOME_DESCR,
    },
    GROUP_INSTANCE_SHELTER_ID: {
        'name': GROUP_INSTANCE_SHELTER_NAME,
        'description': GROUP_INSTANCE_SHELTER_DESCR,
    },
    GROUP_INSTANCE_DEAD_ID: {
        'name': GROUP_INSTANCE_DEAD_NAME,
        'description': GROUP_INSTANCE_DEAD_DESCR,
    },
}
PRIVATE_GROUP = (
    GROUP_INSTANCE_DEAD_ID,
)
GALLERY_DEFAULT_ITEMS_COUNT = 9
PAGE = 'page'
PER_PAGE = 'per_page'
PER_PAGE_ALL = 'all'

SHOW_FILTER_KEY = 'filter'


def get_group(group_id, show_permission=False):
    if group_id in GROUP_MAPPING:
        if show_permission is False and group_id in PRIVATE_GROUP:
            raise Http404('Нет прав для просмотра данной группы.')
        return Group.get_group_with_certain_settings(name=GROUP_MAPPING[group_id]['name'],
                                                     group_id=group_id,
                                                     description=GROUP_MAPPING[group_id]['description'])
    else:
        query = dict()
        query['id'] = group_id
        if show_permission is False:
            query['show'] = True
        res = get_object_or_404(Group, **query)
        return res


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


def get_default_group_list(show_permission=False):
    default_group_list = list()
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_ALL_ID, show_permission=show_permission))
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_SHELTER_ID, show_permission=show_permission))
    default_group_list.append(get_group(group_id=GROUP_INSTANCE_HOME_ID, show_permission=show_permission))
    if show_permission:
        default_group_list.append(get_group(group_id=GROUP_INSTANCE_DEAD_ID, show_permission=show_permission))
    return default_group_list


def get_base_context(active_menu, show_permission=False):
    default_group_list = get_default_group_list(show_permission=show_permission)
    user_group_list = get_groups_from_query(dict(), show_permission=show_permission)

    animal_filter_url = dict()
    animal_filter_url['caption'] = 'Поиск'
    animal_filter_url['url'] = "{url}?{key}=1".format(url=reverse(URL_NAME_ANIMALS), key=SHOW_FILTER_KEY)

    find_cat_url = dict()
    find_cat_url['caption'] = ARTICLES_DEFAULT[ARTICLE_FIND_CAT_ID]
    find_cat_url['url'] = reverse(URL_NAME_FIND_CAT)

    articles = [find_cat_url] + list(Subject.objects.all())

    context = {
        'group_list': [animal_filter_url] + default_group_list + list(user_group_list),
        'helpful_info_list': articles,
        'active_menu': active_menu
    }
    return context


def get_page(page, paginator):
    try:
        res = paginator.page(page)
    except PageNotAnInteger:
        res = paginator.page(1)
    except EmptyPage:
        res = paginator.page(paginator.num_pages)
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
        group_list = get_groups_from_query(dict(), show_permission=show_permission)
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
