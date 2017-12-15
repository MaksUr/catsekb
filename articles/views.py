# Create your views here.
from django.views.generic import DetailView, ListView

from articles.article_constants import ARTICLE_CONTACTS_ID, ARTICLE_TITLE, ARTICLES_DEFAULT_MAPPING, \
    ARTICLE_FIND_CAT_ID, \
    CAPTION
from articles.models import Subject, Article, News
from catsekb.constants import ARTICLES, CONTACTS, DJ_ID, URL_NAME_SUBJECTS_TITLE, URL_NAME_SUBJECT_TITLE, \
    URL_NAME_ARTICLE_TITLE, SHOW, CREATED, URL_NAME_NEWS_FEED_TITLE, URL_NAME_ARTICLES_FEED_TITLE, GET_PAR_KEY_PER_PAGE, \
    GET_PAR_VAL_PAGE, GET_PAR_KEY_PAGE
from catsekb.view_functions import get_base_context, get_objects_from_query


class AbstractFeedListView(ListView):
    paginate_by = 30
    title = ''
    order_by = None

    def get_queryset(self):
        return get_objects_from_query(
            model_cls=self.model,
            query=dict(),
            show_permission=self.request.user.is_authenticated(),
            order_by=self.order_by
        )

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = super(AbstractFeedListView, self).get_context_data(**kwargs)
        context.update(get_base_context(show_permission=show_permission, active_menu=ARTICLES, extra_title=self.title))
        context['caption'] = self.title
        return context

    def get_paginate_by(self, queryset):
        per_page = self.request.GET.get(GET_PAR_KEY_PER_PAGE)
        if per_page is not None:
            if per_page == GET_PAR_VAL_PAGE:
                self.kwargs[GET_PAR_KEY_PAGE] = 1
                return len(queryset)
            else:
                try:
                    return int(per_page)
                except ValueError:
                    return self.paginate_by
        else:
            return self.paginate_by


class SubjectListView(AbstractFeedListView):
    model = Subject
    title = URL_NAME_SUBJECTS_TITLE
    order_by = 'id'

    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data(**kwargs)
        article, updated = Article.objects.get_or_create(
            id=ARTICLE_FIND_CAT_ID, defaults={
                ARTICLE_TITLE: ARTICLES_DEFAULT_MAPPING[ARTICLE_FIND_CAT_ID][CAPTION],
                DJ_ID: ARTICLE_FIND_CAT_ID
            }
        )
        context['find_cat'] = article
        return context


class NewsFeedListView(AbstractFeedListView):
    model = News
    title = URL_NAME_NEWS_FEED_TITLE
    template_name = 'articles/feed_list.html'
    order_by = '-created'


class ArticlesFeedListView(AbstractFeedListView):
    model = Article
    title = URL_NAME_SUBJECTS_TITLE
    template_name = 'articles/feed_list.html'
    order_by = '-created'


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


class AbstractArticleDetailView(DetailView):
    active_menu = ARTICLES
    template_name = 'articles/article_detail.html'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated() is not True:
            queryset = self.model.objects.filter(**{SHOW: True})
        obj = super(AbstractArticleDetailView, self).get_object(queryset=queryset)
        return obj

    def get_context_data(self, **kwargs):
        show_permission = self.request.user.is_authenticated()
        context = DetailView.get_context_data(self, **kwargs)
        context.update(
            get_base_context(
                show_permission=show_permission,
                active_menu=self.active_menu,
                extra_title=self.object.title
            )
        )
        q = dict()
        if show_permission is not True:
            q[SHOW] = True
        context['next'] = self.model.objects.filter(id__gt=self.object.id).order_by('id').first()
        context['previous'] = self.model.objects.filter(id__lt=self.object.id).order_by('-id').first()
        # TODO: проверить первые и последние
        return context


class ArticleDetailView(AbstractArticleDetailView):
    model = Article


class NewsDetailView(AbstractArticleDetailView):
    model = News


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
