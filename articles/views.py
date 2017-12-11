# Create your views here.
from django.views.generic import DetailView, ListView

from articles.article_constants import ARTICLE_CONTACTS_ID, ARTICLE_TITLE, ARTICLES_DEFAULT_MAPPING, ARTICLE_FIND_CAT_ID, \
    CAPTION
from articles.models import Subject, Article
from catsekb.constants import ARTICLES, CONTACTS, DJ_ID, URL_NAME_SUBJECTS_TITLE, URL_NAME_SUBJECT_TITLE, \
    URL_NAME_ARTICLE_TITLE, SHOW
from catsekb.view_functions import get_base_context, get_objects_from_query


class SubjectListView(ListView):
    model = Subject

    def get_queryset(self):
        return get_objects_from_query(
            model_cls=Subject,
            query=dict(),
            show_permission=self.request.user.is_authenticated()
        )

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = ListView.get_context_data(self, **kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ARTICLES, extra_title=URL_NAME_SUBJECTS_TITLE))
        article, updated = Article.objects.get_or_create(
            id=ARTICLE_FIND_CAT_ID, defaults={
                ARTICLE_TITLE: ARTICLES_DEFAULT_MAPPING[ARTICLE_FIND_CAT_ID][CAPTION],
                DJ_ID: ARTICLE_FIND_CAT_ID
            }
        )
        context['find_cat'] = article
        return context


class SubjectDetailView(DetailView):
    model = Subject

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated() is not True:
            queryset = Subject.objects.filter(**{SHOW: True})
        obj = super(SubjectDetailView, self).get_object(queryset=queryset)
        return obj

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(
            get_base_context(
                show_permission=show_permission,
                active_menu=ARTICLES,
                extra_title=URL_NAME_SUBJECT_TITLE.format(subj=self.object.name)))
        return context


class ArticleDetailView(DetailView):
    model = Article
    active_menu = ARTICLES

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated() is not True:
            queryset = Subject.objects.filter(**{SHOW: True})
        obj = super(ArticleDetailView, self).get_object(queryset=queryset)
        return obj

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(
            get_base_context(
                show_permission=show_permission,
                active_menu=self.active_menu,
                extra_title=URL_NAME_ARTICLE_TITLE.format(title=self.object.title)
            )
        )
        return context


class DefaultArticleDetailView(ArticleDetailView):
    article_id = None  # abstract

    def get_object(self, queryset=None):
        title = ARTICLES_DEFAULT_MAPPING.get(self.article_id)
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
