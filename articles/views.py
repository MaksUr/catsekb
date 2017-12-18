# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import DetailView, ListView

from articles.article_constants import ARTICLE_CONTACTS_ID, ARTICLE_TITLE, ARTICLES_DEFAULT_MAPPING, \
    ARTICLE_FIND_CAT_ID, \
    CAPTION, ARTICLE_TEXT
from articles.models import Subject, Article, News
from catsekb.constants import ARTICLES, CONTACTS, DJ_ID, URL_NAME_SUBJECTS_TITLE, URL_NAME_SUBJECT_TITLE, \
    SHOW, URL_NAME_NEWS_FEED_TITLE, GET_PAR_KEY_PER_PAGE, \
    GET_PAR_VAL_PAGE, GET_PAR_KEY_PAGE
from catsekb.view_functions import get_base_context, get_objects_from_query


class AbstractFeedListView(ListView):
    paginate_by = 3
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

    def get_queryset(self):
        queryset = super(ArticlesFeedListView, self).get_queryset()
        return queryset.exclude(**{'id__in': list(ARTICLES_DEFAULT_MAPPING)})


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
    pagination_order = 'created'

    def get_object(self, queryset=None):
        queryset = self.queryset or self.get_queryset() or queryset
        obj = super(AbstractArticleDetailView, self).get_object(queryset=queryset)
        return obj

    def get_queryset(self):
        query_d = {}
        if self.request.user.is_authenticated() is not True:
            query_d[SHOW] = True
        self.queryset = self.model.objects.filter(**query_d)
        return self.queryset

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
        if self.pagination_order:
            context['page'] = self.get_page()
        return context

    def get_page(self):
        if self.pagination_order:
            articles = self.get_queryset().order_by(self.pagination_order)
        else:
            articles = self.get_queryset()
        for index, art in enumerate(articles):
            page_numb = index + 1
            if art.id == int(self.kwargs['pk']):
                current_page = page_numb
                break
        else:
            return None
        paginator = Paginator(articles, 1)
        page = paginator.page(current_page)
        return page


class ArticleDetailView(AbstractArticleDetailView):
    model = Article

    def get_queryset(self):
        queryset = super(ArticleDetailView, self).get_queryset()
        self.queryset = queryset.exclude(**{'id__in': list(ARTICLES_DEFAULT_MAPPING)})
        return self.queryset


class NewsDetailView(AbstractArticleDetailView):
    model = News


class DefaultArticleDetailView(AbstractArticleDetailView):
    article_id = None  # abstract
    pagination_order = None
    model = Article

    def get_queryset(self):
        queryset = super(DefaultArticleDetailView, self).get_queryset()
        self.queryset = queryset.filter(**{'id__in': list(ARTICLES_DEFAULT_MAPPING)})
        return self.queryset

    def save_default_article(self):
        # TODO: check
        default_art = ARTICLES_DEFAULT_MAPPING.get(self.article_id)
        if default_art is not None:
            article, created = Article.objects.get_or_create(
                id=self.article_id, defaults={
                    ARTICLE_TITLE: default_art[CAPTION],
                    DJ_ID: self.article_id,
                    ARTICLE_TEXT: '<p>Страница в разработке<p>'
                }
            )
            return article
        else:
            raise Http404('Внутреняя ошибка.')

    def get_object(self, queryset=None):
        self.kwargs['pk'] = self.article_id
        try:
            obj = self.get_queryset().get(id=self.article_id)
        except ObjectDoesNotExist:
            obj = self.save_default_article()
        return obj


class ContactsView(DefaultArticleDetailView):
    template_name = 'articles/contacts.html'
    active_menu = CONTACTS
    article_id = ARTICLE_CONTACTS_ID


class FindCatView(DefaultArticleDetailView):
    article_id = ARTICLE_FIND_CAT_ID
