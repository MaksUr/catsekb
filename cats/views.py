from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cats.cats_constants import \
    ANIMAL_LOCATION_STATUS, \
    GROUP_ANIMALS_PREVIEW_COUNT, GALLERY_DEFAULT_ITEMS_COUNT
from cats.forms import FilterForm
from cats.models import Animal, Group
from cats.query import ANIMAL_QUERY_KEYS
from catsekb.constants import ANIMALS, GET_PAR_KEY_PAGE, GET_PAR_KEY_PER_PAGE, \
    GET_PAR_VAL_PAGE, \
    GET_PAR_KEY_FILTER, DJ_OBJECT, URL_NAME_GROUP, NAME, DESCRIPTION, URL_NAME_GROUPS_TITLE
from catsekb.view_functions import get_objects_from_query, get_base_catsekb_context, get_group, get_animals_from_query, \
    get_shelter_animals


class AnimalListView(ListView, FormMixin):
    paginate_by = 9
    model = Animal
    form_class = FilterForm
    caption = 'Наши питомцы'
    description = None
    show_filter = False
    project = None
    location_status = None

    def get_queryset(self, **kwargs):
        query = self.request.GET.dict()
        query.update(kwargs)
        if self.project is not None:
            query.update({'project': self.project})
        if self.location_status is not None and self.location_status in ['S', 'H', 'D']:
            query.update({'location_status': self.location_status})
        self.show_filter = query.pop(GET_PAR_KEY_FILTER, False)
        if self.show_filter and not(set(query) & set(ANIMAL_QUERY_KEYS)):
            res = Animal.objects.none()
        else:
            res = get_animals_from_query(query, show_permission=True)
        return res

    def get_context_data(self, **kwargs):
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
        extra_title = context['caption']
        context.update(get_base_catsekb_context(active_menu=ANIMALS, extra_title=extra_title))
        return context

    def get_filter_string(self):
        query = self.request.GET.copy()
        query._mutable = True
        if self.show_filter:
            query['filter'] = 1  # Ключ в GET параметра, включающий поиск по галереи.
        if not query:
            return ''
        return '?' + query.urlencode()

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
    template_name = 'catsekb_page/animal_detail.html'
    model = Animal

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated
        context = DetailView.get_context_data(self, **kwargs)
        context.update(get_base_catsekb_context(active_menu=ANIMALS, extra_title=self.object.__str__()))
        animal = kwargs[DJ_OBJECT]
        if show_permission is False and animal.show is False:
            raise Http404("Нет прав для просмотра этой страницы")
        animals_query = self.get_animals_query()
        if animals_query:
            animals = get_animals_from_query(animals_query, show_permission=True)
            context['page'] = self.get_animal_page(animals, animal)
        shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=True, count=9)
        context['shelter_animals'] = shelter_animals
        context['shelter_caption'] = 'Ищут дом'
        return context

    def get_animals_query(self):
        res = self.request.GET.dict()
        return res

    @staticmethod
    def get_animal_page(animals, animal):
        if animal not in animals:
            return None
        else:
            try:
                page_number = list(animals).index(animal) + 1
            except ValueError:
                return None
            paginator = Paginator(animals, 1)
            page = paginator.page(page_number)
            return page


class GroupListView(ListView):
    # template_name = 'cats/group_list.html'
    # model = Group
    # TODO: сделать обычную View

    def get_queryset(self):
        group_list = get_objects_from_query(model_cls=Group, query=dict(), show_permission=True)
        return group_list

    def get_context_data(self, **kwargs):
        context = {}
        context.update(get_base_catsekb_context(active_menu=ANIMALS, extra_title=URL_NAME_GROUPS_TITLE))

        context['shelter_caption'] = 'Ищут дом'
        context['shelter_url'] = reverse(URL_NAME_GROUP, kwargs={'pk': 'S'})
        context['shelter_animals'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: 'S'},
            show_permission=True
        ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        context['home_caption'] = 'Пристроены'
        context['home_url'] = reverse(URL_NAME_GROUP, kwargs={'pk': 'H'})
        context['home_animals'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: 'H'},
            show_permission=True
        ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        context['dying_caption'] = 'На радуге'
        context['dying_url'] = reverse(URL_NAME_GROUP, kwargs={'pk': 'D'})
        context['dying_animals'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: 'D'},
            show_permission=True
        ).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]

        context['groups'] = get_objects_from_query(model_cls=Group, query=dict(), show_permission=True)
        return context


class GroupDetailView(AnimalListView):

    def set_description_and_caption(self, query):
        group = get_group(group_id=self.kwargs['pk'], show_permission=True)
        self.description = group.description
        self.caption = group.name

    def get_queryset(self):
        res = super(GroupDetailView, self).get_queryset(group_id=self.kwargs['pk'])
        return res

    def get_context_data(self, **kwargs):
        group_id = self.kwargs['pk']
        group = get_group(group_id=group_id, show_permission=True)
        self.caption = group.name
        self.description = group.description
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        return context
