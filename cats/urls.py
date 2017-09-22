from django.conf.urls import url

from cats.constants import URL_NAME_GROUP, URL_NAME_ANIMAL, URL_NAME_INDEX
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^group_(?P<group_id>[0-9a-z]+)/animal_(?P<animal_id>[0-9]+)/$', views.animal, name='animal'),
    url(r'^animal_(?P<animal_id>[0-9]+)/$', views.animal, name='animal'),  # TODO: Объединить animal
    url(r'^group_(?P<group_id>[0-9a-z]+)/$', views.group, name='group'),
]
