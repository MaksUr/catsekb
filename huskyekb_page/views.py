from django.shortcuts import render
from constance import config

from catsekb.view_functions import get_shelter_animals, get_home_animals_count


def huskyekb_page_view(request):
    show_permission = request.user.is_authenticated
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=show_permission, project='huskyekb')
    home_animals_count = get_home_animals_count(project='huskyekb') + config.HUSKY_COUNT_CORRECTION
    context = {
        'shelter_animals': shelter_animals,
        'shelter_animals_count': shelter_animals_count,
        'home_animals_count': home_animals_count,

    }
    return render(request, 'huskyekb_page/index.html', context)
