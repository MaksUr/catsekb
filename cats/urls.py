from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),

    url(r'^group_list/$', views.GroupListView.as_view(), name='group_list'),
    url(r'^group_(?P<pk>[0-9al]+)/$', views.GroupDetailView.as_view(), name='group_detail'),

    url(r'^animal_list/$', views.AnimalListView.as_view(), name='animal_list'),
    url(r'^animal_(?P<pk>[0-9]+)/$', views.AnimalDetailView.as_view(), name='animal_detail'),

    url(r'^group_(?P<group_pk>[0-9al]+)/animal_(?P<pk>[0-9]+)/$', views.AnimalDetailView.as_view(), name='animal_detail'),
]
