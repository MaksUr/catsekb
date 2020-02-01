from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('articles/list/', views.SubjectListView.as_view(), name='article_list'),

    path('news/', views.NewsFeedListView.as_view(), name='news'),    

    url(r'^feed/$', views.ArticlesFeedListView.as_view(), name='subjects_feed'),
    url(r'^subject_(?P<pk>[0-9]+)$', views.SubjectDetailView.as_view(), name='subject'),
    url(r'^article_(?P<pk>[0-9]+)$', views.ArticleDetailView.as_view(), name='article'),
    url(r'^post_(?P<pk>[0-9]+)$', views.NewsDetailView.as_view(), name='post'),
    url(r'^find_cat/$', views.FindCatView.as_view(), name='find_cat'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    path('video/', views.AnimalVideoListView.as_view(), name='video'),
]
