from constance import config
from django.shortcuts import render

from catsekb.view_functions import get_shelter_animals, get_home_animals_count, get_base_catsekb_context, \
    get_animals_from_query


def huskyekb_page_view(request):
    context = get_base_catsekb_context(active_menu='index', extra_title='Главная страница', project='huskyekb')
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=True, project='huskyekb')
    context['shelter_animals'] = shelter_animals
    context['shelter_animals_count'] = shelter_animals_count
    # context['articles'] = get_last_articles(2)
    context['home_animals_count'] = get_home_animals_count(project='huskyekb') + config.HUSKY_COUNT_CORRECTION
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    return render(request, 'huskyekb_page/index.html', context)
