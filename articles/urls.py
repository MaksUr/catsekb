from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SubjectListView.as_view(), name='subjects'),
    url(r'^feed/$', views.ArticlesFeedListView.as_view(), name='subjects_feed'),
    url(r'^subject_(?P<pk>[0-9]+)$', views.SubjectDetailView.as_view(), name='subject'),
    url(r'^article_(?P<pk>[0-9]+)$', views.ArticleDetailView.as_view(), name='article'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    url(r'^find_cat/$', views.FindCatView.as_view(), name='find_cat'),
]
