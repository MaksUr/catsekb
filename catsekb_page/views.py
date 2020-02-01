from constance import config
from django.shortcuts import render

from catsekb.constants import INDEX
from catsekb.view_functions import get_base_catsekb_context, get_important_news, get_animals_from_query, \
    get_last_articles, get_shelter_animals, get_home_animals_count


def catsekb_page_view(request):
    show_permission = request.user.is_authenticated
    context = get_base_catsekb_context(show_permission=show_permission, active_menu=INDEX, extra_title='Главная страница')
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=show_permission, project='catsekb')
    context['shelter_animals'] = shelter_animals
    context['shelter_animals_count'] = shelter_animals_count
    context['important_news'] = get_important_news()
    context['articles'] = get_last_articles(2)
    context['home_animals_count'] = get_home_animals_count(project='catsekb') + config.CATS_COUNT_CORRECTION
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    return render(request, 'catsekb_page/index.html', context)
