from django.conf.urls import url
from django.urls import path, register_converter

from .urls_converters import ProjectConverter
from . import views

register_converter(ProjectConverter, 'project')

urlpatterns = [
    path('', views.AnimalListView.as_view(template_name='cats/animal_list.html'), name='animal_list'),  # TODO: rename name to "pets_all"
    path(
        'shelter/',
        views.AnimalListView.as_view(template_name='cats/animal_list.html'),
        name='pets_in_shelter',
        # caption='',  # TODO
        # description='',  # TODO
        # location_status=''  # TODO
    ),
    path(
        'home/',
        views.AnimalListView.as_view(template_name='cats/animal_list.html'),
        name='pets_in_home',
        # caption='',  # TODO
        # description='',  # TODO
        # location_status=''  # TODO
    ),
    path(
        'rainbow/',
        views.AnimalListView.as_view(template_name='cats/animal_list.html'),
        name='pets_dead',
        # caption='',  # TODO
        # description='',  # TODO
        # location_status=''  # TODO
    ),
    path('groups/', views.GroupListView.as_view(template_name='cats/group_list.html'), name='group_list'),
    url(r'^group_(?P<pk>([0-9]+)|(all)|(S)|(H)|(D))/$', views.GroupDetailView.as_view(), name='group_detail'),
    path('<project:project>/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),  #  TODO: поменять project и pets местами
]
