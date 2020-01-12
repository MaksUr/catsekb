from django.urls import path, include
from articles.views import NewsFeedListView, AnimalVideoListView
from catsekb.constants import CATSEKB_PAGE
from catsekb_page.views import catsekb_page_view

urlpatterns = [
    path('', catsekb_page_view, name=CATSEKB_PAGE),
    path('cats/', include('cats.urls')),
    path('news/', NewsFeedListView.as_view(), name='news_feed'),
    path('video/', AnimalVideoListView.as_view(), name='video'),
    path('articles/', include('articles.urls')),
]
