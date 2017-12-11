from django.contrib import admin

from articles.article_constants import ARTICLE_TITLE, ARTICLE_SHOW, SUBJECT_SHOW, SUBJECT_NAME
from articles.models import Article, Author, Subject


class ArticleAdmin(admin.ModelAdmin):
    list_display = (ARTICLE_TITLE, ARTICLE_SHOW)
admin.site.register(Article, ArticleAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (SUBJECT_NAME, SUBJECT_SHOW)
admin.site.register(Subject, SubjectAdmin)

admin.site.register(Author)


