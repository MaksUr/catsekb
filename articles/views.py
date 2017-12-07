# Create your views here.
from django.views.generic import DetailView, ListView

from articles.article_constants import ARTICLE_CONTACTS_ID, ARTICLE_TITLE, ARTICLES_DEFAULT, ARTICLE_FIND_CAT_ID, \
    CAPTION
from articles.models import Subject, Article
from catsekb.constants import ARTICLES, CONTACTS, DJ_ID
from catsekb.view_functions import get_base_context


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
    active_menu = ARTICLES

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=self.active_menu))
        return context


class DefaultArticleDetailView(ArticleDetailView):
    article_id = None  # abstract

    def get_object(self, queryset=None):
        title = ARTICLES_DEFAULT.get(self.article_id)
        if title is not None:
            article, updated = Article.objects.get_or_create(
                id=self.article_id, defaults={ARTICLE_TITLE: title[CAPTION], DJ_ID: self.article_id})
            return article
        else:
            return None


class ContactsView(DefaultArticleDetailView):
    template_name = 'articles/contacts.html'
    active_menu = CONTACTS
    article_id = ARTICLE_CONTACTS_ID


class FindCatView(DefaultArticleDetailView):
    article_id = ARTICLE_FIND_CAT_ID
