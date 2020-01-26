from constance import config
from django.shortcuts import render

from cats.cats_constants import ANIMAL_VIDEO_PUT_TO_INDEX_PAGE
from cats.models import AnimalVideo
from catsekb.constants import URL_NAME_INDEX_TITLE, INDEX, CREATED
from catsekb.view_functions import get_base_catsekb_context, get_important_news, get_animals_from_query, \
    get_last_articles, get_objects_from_query, get_shelter_animals, get_home_animals_count


def catsekb_page_view(request):
    show_permission = request.user.is_authenticated
    context = get_base_catsekb_context(show_permission=show_permission, active_menu=INDEX, extra_title=URL_NAME_INDEX_TITLE)
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=show_permission)
    context['shelter_animals'] = shelter_animals
    context['shelter_animals_count'] = shelter_animals_count
    context['important_news'] = get_important_news()
    context['articles'] = get_last_articles(2)
    context['home_animals_count'] = get_home_animals_count() + config.CATS_COUNT_CORRECTION
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    # TODO: add main parameter
    context['main_video'] = get_objects_from_query(
        model_cls=AnimalVideo, query={ANIMAL_VIDEO_PUT_TO_INDEX_PAGE: True},
        show_permission=show_permission,
        order_by='-'+CREATED,
    )
    return render(request, 'catsekb_page/index.html', context)
