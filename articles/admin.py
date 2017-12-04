from django.contrib import admin

from articles.models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, ArticleAdmin)
admin.site.register(Article)

