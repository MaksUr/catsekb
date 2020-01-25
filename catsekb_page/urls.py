from django.urls import path, include
from articles.views import NewsFeedListView, AnimalVideoListView
from catsekb_page.views import catsekb_page_view

urlpatterns = [
    path('', catsekb_page_view, name='catsekb_page'),
    path('cats/', include('cats.urls')),
    path('news/', NewsFeedListView.as_view(), name='news_feed'),
    path('video/', AnimalVideoListView.as_view(), name='video'),
    path('articles/', include('articles.urls')),
]
