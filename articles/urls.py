from django.conf.urls import url

from articles.article_constants import ARTICLE_CONTACTS_ID, ARTICLE_FIND_CAT_ID
from cats.cats_constants import DJ_PK
from . import views

urlpatterns = [
    url(r'^$', views.SubjectListView.as_view(), name='subjects'),
    url(r'^subject_(?P<pk>[0-9]+)$', views.SubjectDetailView.as_view(), name='subject'),
    url(r'^article_(?P<pk>[0-9]+)$', views.ArticleDetailView.as_view(), name='article'),
    url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    url(r'^find_cat/$', views.FindCatView.as_view(), name='find_cat'),
]
