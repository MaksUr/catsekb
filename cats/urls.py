from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^animal_(?P<animal_id>[0-9]+)/$', views.animal, name='animal'),
]