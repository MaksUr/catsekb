from django.urls import path, include

from cats.views import GroupDetailView
from huskyekb_page.views import huskyekb_page_view

urlpatterns = [
    path('', huskyekb_page_view, name='huskyekb_page'),
    path(
        'gallery/',
        GroupDetailView.as_view(template_name='huskyekb_page/animal_list.html', project='huskyekb'),
        {'pk': 'S'},
        name='husky_looking_for_home'
    )
]
