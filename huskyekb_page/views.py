from django.shortcuts import render

from catsekb.view_functions import get_shelter_animals


def huskyekb_page_view(request):
    show_permission = request.user.is_authenticated
    shelter_animals, shelter_animals_count = get_shelter_animals(show_permission=show_permission, project='huskyekb')
    return render(request, 'huskyekb_page/index.html', {'shelter_animals': shelter_animals})
