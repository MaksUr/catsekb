from django.urls import path

from cats.views import AnimalListView
from catsekb_page.views import catsekb_page_view

urlpatterns = [
    path('', catsekb_page_view, name='catsekb_page'),
    path('pets/', AnimalListView.as_view(
        template_name='catsekb_page/animal_list.html',
        caption='Все котики',
        description='Все котики, которые попали к нам в приют.',
        location_status=None,
        project='catsekb',
    ), name='cats_all'),
    path('pets/shelter/', AnimalListView.as_view(
        template_name='catsekb_page/animal_list.html',
        caption='Ищут дом',
        description='Собаки привязываются к людям, кошки привязываются к дому. Не дай этим котикам привязаться к клетке. Помоги им обрести свой дом.',
        location_status='S',
        project='catsekb',
    ), name='cats_in_shelter'),
    path('pets/home/', AnimalListView.as_view(
        template_name='catsekb_page/animal_list.html',
        caption='Пристроены',
        description='Они обрели свой дом',
        location_status='H',
        project='catsekb',
    ), name='cats_in_home'),
    path('pets/rainbow/', AnimalListView.as_view(
        template_name='catsekb_page/animal_list.html',
        caption='На радуге',
        description='Пусть земля им будет пухом, они всегда останутся в наших сердцах.',
        location_status='D',
        project='catsekb',
    ), name='cats_dead'),
]
