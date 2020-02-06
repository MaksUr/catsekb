from django.urls import path

from cats.views import AnimalListView
from rotvodom_page.views import rotvodom_page_view

urlpatterns = [
    path('', rotvodom_page_view, name='rotvodom_page'),

    path('pets/', AnimalListView.as_view(
        template_name='rotvodom_page/animal_list.html',
        caption='Все ротвейлеры',
        description='Все питомцы, которые попали к нам в приют.',
        location_status=None,
        project='rotvodom',
    ), name='rotv_all'),
    path('pets/shelter/', AnimalListView.as_view(
        template_name='rotvodom_page/animal_list.html',
        caption='Ищут дом',
        description='Помоги им обрести свой дом.',
        location_status='S',
        project='rotvodom',
    ), name='rotv_in_shelter'),
    path('pets/home/', AnimalListView.as_view(
        template_name='rotvodom_page/animal_list.html',
        caption='Пристроены',
        description='Они обрели свой дом',
        location_status='H',
        project='rotvodom',
    ), name='rotv_in_home'),
    path('pets/rainbow/', AnimalListView.as_view(
        template_name='rotvodom_page/animal_list.html',
        caption='На радуге',
        description='Пусть земля им будет пухом, они всегда останутся в наших сердцах.',
        location_status='D',
        project='rotvodom',
    ), name='rotv_dead'),
]
