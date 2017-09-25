from django.conf.urls import url

from cats.constants import URL_NAME_GROUP, URL_NAME_ANIMAL, URL_NAME_INDEX, URL_NAME_GROUPS
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^group_(?P<group_id>[0-9a-z]+)/animal_(?P<animal_id>[0-9]+)/$', views.animal_view, name='animal'),
    url(r'^animal_(?P<animal_id>[0-9]+)/$', views.animal_view, name='animal'),  # TODO: Объединить animal
    url(r'^group_(?P<group_id>[0-9a-z]+)/$', views.group_view, name='group'),
    url(r'^groups/$', views.groups_view, name='groups'),
]
