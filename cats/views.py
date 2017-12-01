from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView

from cats.constants import GROUP_ALL_ANIMALS_NAME, ANIMAL_CREATED, ANIMAL_SHOW, DJ_PK, DJ_PAGE, DJ_OBJECT, \
    GROUP_SHOW, ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_SHELTER, GROUP_ALL_ANIMALS_KEY_NAME, \
    ANIMAL_LOCATION_STATUS_CHOICE_HOME, ANIMAL_LOCATION_STATUS_CHOICE_SHELTER, ANIMAL_LOCATION_STATUS, \
    CAPTION_ANIMAL_LIST_DEFAULT, GROUP_ID, GROUP_ALL_ANIMALS_NAME_DESCR, ANIMAL_LOCATION_STATUS_HOME_DESСR, \
    ANIMAL_LOCATION_STATUS_SHELTER_DESСR, ANIMAL_LOCATION_STATUS_DEAD, ANIMAL_LOCATION_STATUS_CHOICE_DEAD, \
    ANIMAL_LOCATION_STATUS_DEAD_DESСR, INDEX, ANIMALS, URL_NAME_ANIMAL_FILTER
from cats.forms import FilterForm
from cats.models import Animal, Group

GROUP_MAPPING = {
    GROUP_ALL_ANIMALS_NAME: {
        'name': GROUP_ALL_ANIMALS_KEY_NAME,
        'description': GROUP_ALL_ANIMALS_NAME_DESCR,
    },
    ANIMAL_LOCATION_STATUS_HOME: {
        'name': ANIMAL_LOCATION_STATUS_CHOICE_HOME,
        'description': ANIMAL_LOCATION_STATUS_HOME_DESСR,
    },
    ANIMAL_LOCATION_STATUS_SHELTER: {
        'name': ANIMAL_LOCATION_STATUS_CHOICE_SHELTER,
        'description': ANIMAL_LOCATION_STATUS_SHELTER_DESСR,
    },
    ANIMAL_LOCATION_STATUS_DEAD: {
        'name': ANIMAL_LOCATION_STATUS_CHOICE_DEAD,
        'description': ANIMAL_LOCATION_STATUS_DEAD_DESСR,
    },
}
PRIVATE_GROUP = (
    ANIMAL_LOCATION_STATUS_DEAD,
)
GALLERY_DEFAULT_ITEMS_COUNT = 9
PAGE = 'page'
PER_PAGE = 'per_page'
PER_PAGE_ALL = 'all'


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


def get_animals_from_query(query, show_permission=False):
    """

    :rtype: QueryDict
    :type show_permission: bool
    :type query: dict
    """
    query.pop(PAGE, None)
    query.pop(PER_PAGE, None)
    if query.get(PAGE) is not None:
        del query[PAGE]
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


def get_base_context(active_menu, show_permission=False):
    default_group_list = list()
    default_group_list.append(get_group(group_id=GROUP_ALL_ANIMALS_NAME, show_permission=show_permission))
    default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_SHELTER, show_permission=show_permission))
    default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_HOME, show_permission=show_permission))
    if show_permission:
        default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_DEAD, show_permission=show_permission))

    user_group_list = get_groups_from_query(dict(), show_permission=show_permission)
    animal_filter_url = dict()
    animal_filter_url['caption'] = 'Поиск'
    animal_filter_url['url'] = URL_NAME_ANIMAL_FILTER
    context = {
        'group_list': [animal_filter_url] + default_group_list + list(user_group_list),
        'helpful_info_list': (),
        'active_menu': active_menu
    }
    return context


def get_filter_string(query):
    """

    :type query: QueryDict
    """
    if query:
        return '?' + query.urlencode()
    else:
        return ''


def get_page(page, paginator):
    try:
        res = paginator.page(page)
    except PageNotAnInteger:
        res = paginator.page(1)
    except EmptyPage:
        res = paginator.page(paginator.num_pages)
    return res


def get_paginator(object_list, per_page, page_number, context):
    if per_page == PER_PAGE_ALL:
        per_page = len(object_list)
    paginator = Paginator(object_list=object_list, per_page=per_page)
    page = get_page(page=page_number, paginator=paginator)
    context['page_obj'] = page
    context['object_list'] = page.object_list


# TODO: доступен только админам или из фильтра с контролем параметров
class AnimalListView(ListView):
    # template animal_list
    paginate_by = GALLERY_DEFAULT_ITEMS_COUNT
    model = Animal
    template_name = 'cats/animal_list.html'
    caption = CAPTION_ANIMAL_LIST_DEFAULT
    description = ''

    def get_queryset(self):
        show_permission = self.request.user.is_authenticated()
        query = self.request.GET.dict()
        res = get_animals_from_query(query, show_permission=show_permission)
        return res

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS))
        context['filter_string'] = self.get_filter_string()
        context['caption'] = self.caption
        context['description'] = self.description
        return context

    def get_filter_string(self):
        query = self.request.GET
        if query:
            return '?' + query.urlencode()
        else:
            return ''

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True, **kwargs):
        if self.request.GET.dict().get(PER_PAGE) is not None:
            per_page_param = self.request.GET.dict()[PER_PAGE]
            if per_page_param == PER_PAGE_ALL:
                per_page = len(queryset)
            else:
                try:
                    per_page = int(per_page_param)
                except ValueError:
                    pass
        return ListView.get_paginator(self, queryset=queryset, per_page=per_page, orphans=orphans,
                                      allow_empty_first_page=allow_empty_first_page, **kwargs)


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
        query = {
            'group_id': self.kwargs[DJ_PK],
        }
        return get_animals_from_query(query=query, show_permission=self.request.user.is_authenticated())

    def get_context_data(self, **kwargs):
        group_id = self.kwargs[DJ_PK]
        group = get_group(group_id=group_id, show_permission=self.request.user.is_authenticated())
        self.caption = group.name
        self.description = group.description
        context = AnimalListView.get_context_data(self, **kwargs)
        return context

    def get_filter_string(self):
        res = '?{key}={val}'.format(key=GROUP_ID, val=self.kwargs[DJ_PK])
        if self.request.GET:
            res += '&' + self.request.GET.urlencode()
        return res


def index_view(request):
    show_permission = request.user.is_authenticated()
    context = get_base_context(show_permission=show_permission, active_menu=INDEX)
    query = {ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_SHELTER}
    shelter_animals = get_animals_from_query(
        query=query, show_permission=show_permission
    ).order_by('?')
    context['shelter_animals'] = shelter_animals[:GALLERY_DEFAULT_ITEMS_COUNT]
    context['shelter_caption'] = ANIMAL_LOCATION_STATUS_CHOICE_SHELTER
    context['shelter_animals_count'] = shelter_animals.count()
    context['home_animals_count'] = get_animals_from_query(
        query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_HOME}, show_permission=True
    ).count()
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    if show_permission is True:
        context['dying_animals_count'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_DEAD}, show_permission=True
        ).count()
    return render(request, 'cats/index.html', context)


class FilterView(FormView):
    template_name = 'cats/animal_filter.html'
    form_class = FilterForm

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = FormView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ANIMALS))
        query = self.request.GET.dict()
        page_number = query.pop(PAGE, None)
        per_page = query.pop(PER_PAGE, GALLERY_DEFAULT_ITEMS_COUNT)
        if query:
            animals = get_animals_from_query(query, show_permission=show_permission)
            get_paginator(object_list=animals, per_page=per_page, page_number=page_number, context=context)
        context['filter_string'] = get_filter_string(query=self.request.GET)
        return context

    def get_initial(self):
        initial = FormView.get_initial(self)
        return initial

    def get_form_kwargs(self):
        res = FormView.get_form_kwargs(self)
        res['data'] = self.request.GET.dict()
        return res





