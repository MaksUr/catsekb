from django.urls import path

from cats.views import AnimalListView
from huskyekb_page.views import huskyekb_page_view

urlpatterns = [
    path('', huskyekb_page_view, name='huskyekb_page'),

    path('pets/', AnimalListView.as_view(
        template_name='huskyekb_page/animal_list.html',
        caption='Все хаски',
        description='Все питомцы, которые попали к нам в приют.',
        location_status=None,
        project='huskyekb',
    ), name='husky_all'),
    path('pets/shelter/', AnimalListView.as_view(
        template_name='huskyekb_page/animal_list.html',
        caption='Ищут дом',
        description='Помоги им обрести свой дом.',
        location_status='S',
        project='huskyekb',
    ), name='husky_in_shelter'),
    path('pets/home/', AnimalListView.as_view(
        template_name='huskyekb_page/animal_list.html',
        caption='Пристроены',
        description='Они обрели свой дом',
        location_status='H',
        project='huskyekb',
    ), name='husky_in_home'),
    path('pets/rainbow/', AnimalListView.as_view(
        template_name='huskyekb_page/animal_list.html',
        caption='На радуге',
        description='Пусть земля им будет пухом, они всегда останутся в наших сердцах.',
        location_status='D',
        project='huskyekb',
    ), name='husky_dead'),
]
