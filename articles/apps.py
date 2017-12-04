from django.apps import AppConfig

from articles.article_constants import APPLICATION_VERBOSE_NAME


class ArticlesConfig(AppConfig):
    name = 'articles'
    verbose_name = APPLICATION_VERBOSE_NAME
