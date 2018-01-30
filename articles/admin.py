from django.contrib import admin

from articles.article_constants import ARTICLE_SHOW, SUBJECT_SHOW, SUBJECT_NAME, NEWS_SHOW, \
    NEWS_IMPORTANT
from articles.forms import NewsForm, ArticleForm
from articles.models import Article, Author, Subject, News

admin.site.register(Author)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('__str__', ARTICLE_SHOW, 'created', 'updated')
    search_fields = ('__str__',)
admin.site.register(Article, ArticleAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (SUBJECT_NAME, SUBJECT_SHOW)
admin.site.register(Subject, SubjectAdmin)


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('__str__', NEWS_SHOW, NEWS_IMPORTANT, 'created', 'updated')
    search_fields = ('__str__',)
admin.site.register(News, NewsAdmin)


