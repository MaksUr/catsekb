from django.shortcuts import render

from cats.cats_constants import ANIMAL_LOCATION_STATUS_SHELTER, ANIMAL_LOCATION_STATUS, GROUP_INSTANCE_SHELTER_NAME, \
    ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_DEAD, GALLERY_DEFAULT_ITEMS_COUNT
from catsekb.constants import URL_NAME_INDEX_TITLE, INDEX
from catsekb.view_functions import get_base_context, get_important_news, get_animals_from_query, get_last_articles

HOME_ANIMALS_COUNT = 0


def get_shelter_animals(show_permission, count=GALLERY_DEFAULT_ITEMS_COUNT):
    query = {ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_SHELTER}
    shelter_animals = get_animals_from_query(
        query=query, show_permission=show_permission
    ).order_by('?')
    return shelter_animals[:count], len(shelter_animals)


def get_home_animals_count():
    global HOME_ANIMALS_COUNT
    get_animals_from_query(
        query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_HOME}, show_permission=True
    ).count()
    return HOME_ANIMALS_COUNT or get_animals_from_query(
        query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_HOME}, show_permission=True
    ).count()


def index_view(request):
    show_permission = request.user.is_authenticated()
    context = get_base_context(show_permission=show_permission, active_menu=INDEX, extra_title=URL_NAME_INDEX_TITLE)
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=show_permission)
    context['shelter_animals'] = shelter_animals
    context['shelter_caption'] = GROUP_INSTANCE_SHELTER_NAME
    context['shelter_animals_count'] = shelter_animals_count
    context['important_news'] = get_important_news()
    context['articles'] = get_last_articles(2)
    context['home_animals_count'] = get_home_animals_count() + 77
    context['animals_count'] = get_animals_from_query(query=dict(), show_permission=True).count()
    if show_permission is True:
        context['dying_animals_count'] = get_animals_from_query(
            query={ANIMAL_LOCATION_STATUS: ANIMAL_LOCATION_STATUS_DEAD}, show_permission=True
        ).count()
    return render(request, 'cats/index.html', context)