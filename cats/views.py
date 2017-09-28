from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView

from cats.constants import FILTER_LABEL
from cats.forms import FilterForm
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

    def get_queryset(self):
        query = self.request.GET.dict()
        query['show'] = True
        res = Animal.objects.filter_animals(**query)
        return res

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['filter_string'] = self.get_filter_string()
        context['filter_label'] = FILTER_LABEL
        return context

    def get_filter_string(self):
        if self.request.GET:
            return '?'+self.request.GET.urlencode()
        else:
            return ''


class AnimalDetailView(DetailView):
    # template animal_detail
    model = Animal
    animal_paginate_by = 1

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        animal = kwargs['object']
        animals_query = self.get_animals_query()
        if animals_query:
            animals_query['show'] = True
            animals = Animal.objects.filter_animals(**animals_query).order_by('created')
            context['page'] = self.get_animal_page(animals, animal)
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
    all_animals_list = Animal.objects.filter(show=True)
    group_list = Group.objects.filter(show=True)
    filter_label = FILTER_LABEL
    return render(request, 'cats/index.html', locals())


class FilterView(FormView):
    template_name = 'cats/animal_filter.html'
    form_class = FilterForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return FormView.form_valid(self, form)

    def get_context_data(self, **kwargs):
        context = FormView.get_context_data(self, **kwargs)
        return context
