from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from articles.models import Subject, Article
from cats.constants import ARTICLES
from cats.views import get_base_context


class SubjectListView(ListView):
    model = Subject

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ARTICLES))
        return context


class SubjectDetailView(DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ARTICLES))
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ARTICLES))
        return context


