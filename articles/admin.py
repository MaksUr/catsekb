from django.contrib import admin

from articles.article_constants import ARTICLE_TITLE, ARTICLE_SHOW, SUBJECT_SHOW, SUBJECT_NAME, NEWS_TITLE, NEWS_SHOW
from articles.models import Article, Author, Subject, News

admin.site.register(Author)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', ARTICLE_SHOW)
    search_fields = ('__str__',)
admin.site.register(Article, ArticleAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (SUBJECT_NAME, SUBJECT_SHOW)
admin.site.register(Subject, SubjectAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', NEWS_SHOW)
    search_fields = ('__str__',)
admin.site.register(News, NewsAdmin)


