from django.core.exceptions import FieldError
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView

from cats.constants import GROUP_ALL_ANIMALS_NAME, ANIMAL_CREATED, ANIMAL_SHOW, DJ_PK, DJ_PAGE, DJ_OBJECT, \
    GROUP_SHOW, ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_SHELTER, GROUP_ALL_ANIMALS_KEY_NAME, \
    ANIMAL_LOCATION_STATUS_CHOICE_HOME, ANIMAL_LOCATION_STATUS_CHOICE_SHELTER, ANIMAL_LOCATION_STATUS, \
    CAPTION_ANIMAL_LIST_DEFAULT, GROUP_ID, GROUP_ALL_ANIMALS_NAME_DESCR, ANIMAL_LOCATION_STATUS_HOME_DESСR, \
    ANIMAL_LOCATION_STATUS_SHELTER_DESСR, ANIMAL_LOCATION_STATUS_DEAD, ANIMAL_LOCATION_STATUS_CHOICE_DEAD, \
    ANIMAL_LOCATION_STATUS_DEAD_DESСR
from cats.forms import FilterForm
from cats.models import Animal, Group, Article

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


def get_base_context(show_permission=False):
    default_group_list = list()
    default_group_list.append(get_group(group_id=GROUP_ALL_ANIMALS_NAME, show_permission=show_permission))
    default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_SHELTER, show_permission=show_permission))
    default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_HOME, show_permission=show_permission))
    if show_permission:
        default_group_list.append(get_group(group_id=ANIMAL_LOCATION_STATUS_DEAD, show_permission=show_permission))

    user_group_list = get_groups_from_query(dict(), show_permission=show_permission)
    context = {
        'group_list': default_group_list + list(user_group_list),
        'helpful_info_list': Article.objects.all(),
        # 'header_class': None  TODO: implement different background
    }
    return context


# TODO: доступен только админам или из фильтра с контролем параметров
class AnimalListView(ListView):
    # template animal_list
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
        context.update(get_base_context(show_permission=show_permission))
        context['filter_string'] = self.get_filter_string()
        context['caption'] = self.caption
        context['description'] = self.description
        return context

    def get_filter_string(self):
        """

        :type query: QueryDict
        """
        query = self.request.GET
        if query:
            return '?' + query.urlencode()
        else:
            return ''


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal
    animal_paginate_by = 1

    def get_context_data(self, **kwargs):
        # TODO: add base_context
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


# TODO: Create new app
def InfoDetailView(request, pk):
    return HttpResponse('InfoDetailView')


class GroupListView(ListView):
    # template group_list
    model = Group

    def get_queryset(self):
        show_permission = self.request.user.is_authenticated()
        group_list = get_groups_from_query(dict(), show_permission=show_permission)
        return group_list

    # TODO: add base_context


class GroupDetailView(AnimalListView):

    def get_queryset(self):
        return Animal.objects.filter(group_id=self.kwargs[DJ_PK], show=self.request.user.is_authenticated())

    def get_context_data(self, **kwargs):
        group_id = self.kwargs[DJ_PK]
        group = get_group(group_id=group_id, show_permission=self.request.user.is_authenticated())
        self.caption = group.name
        self.description = group.description
        context = AnimalListView.get_context_data(self, **kwargs)
        return context

    def get_filter_string(self):
        return '?{key}={val}'.format(key=GROUP_ID, val=self.kwargs[DJ_PK])


def index_view(request):
    show_permission = request.user.is_authenticated()
    context = get_base_context(show_permission=show_permission)
    query = {ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_SHELTER}
    # TODO: только с избранными изображениями
    shelter_animals = get_animals_from_query(query=query, show_permission=show_permission)
    context['shelter_animals'] = shelter_animals
    context['shelter_caption'] = ANIMAL_LOCATION_STATUS_CHOICE_SHELTER
    return render(request, 'cats/index.html', context)


class FilterView(FormView):
    template_name = 'cats/animal_filter.html'
    form_class = FilterForm

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = FormView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission))
        if self.request.GET.dict():
            query = self.request.GET
            context['animals'] = get_animals_from_query(query.dict(), show_permission=show_permission)
            # context['filter_string'] = get_filter_string(query) TODO: edit
        return context

    def get_initial(self):
        initial = FormView.get_initial(self)
        initial['sex'] = ''
        initial['age_distance'] = ''
        initial['location_status'] = ''
        return initial

    def get_form_kwargs(self):
        res = FormView.get_form_kwargs(self)
        res['data'] = self.request.GET.dict()
        return res
