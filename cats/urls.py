from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AnimalListView.as_view(), name='animal_list'),
    url(r'^groups/$', views.GroupListView.as_view(), name='group_list'),
    url(r'^group_(?P<pk>([0-9]+)|(all)|(S)|(H)|(D))/$', views.GroupDetailView.as_view(), name='group_detail'),
    url(r'^cat_(?P<pk>[0-9]+)/$', views.AnimalDetailView.as_view(), name='animal_detail'),
]
