from django.urls import path, include
from articles.views import AnimalVideoListView
from cats.views import GroupDetailView
from catsekb_page.views import catsekb_page_view

urlpatterns = [
    path('', catsekb_page_view, name='catsekb_page'),
    path('cats/', include('cats.urls')),
    path(
        'gallery/',
        GroupDetailView.as_view(template_name='catsekb_page/animal_list.html', project='catsekb'),
        {'pk': 'S'},
        name='cats_looking_for_home'
    ),
    path('video/', AnimalVideoListView.as_view(), name='video'),    
]
