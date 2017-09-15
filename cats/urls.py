from django.conf.urls import url

from cats.constants import URL_NAME_GROUP, URL_NAME_ANIMAL, URL_NAME_INDEX
from . import views

urlpatterns = [
    url(r'^$', views.index, name=URL_NAME_INDEX),
    url(r'^animal_(?P<animal_id>[0-9]+)/$', views.animal, name=URL_NAME_ANIMAL),
    url(r'^group_(?P<group_id>[0-9]+)/$', views.group, name=URL_NAME_GROUP),
]
