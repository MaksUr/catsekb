from django.contrib import admin

from articles.article_constants import ARTICLE_SHOW, SUBJECT_SHOW, SUBJECT_NAME, NEWS_SHOW, \
    NEWS_IMPORTANT, ARTICLE_TEXT, NEWS_TEXT, ARTICLE_CREATED, ARTICLE_UPDATED, NEWS_CREATED, NEWS_UPDATED, \
    ARTICLE_TITLE, NEWS_TITLE
from articles.forms import NewsForm, ArticleForm, PartnerEventAdminForm
from articles.models import Article, Author, Subject, News, Results, PartnerEvent, Partner

admin.site.register(Author)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('__str__', ARTICLE_SHOW, ARTICLE_CREATED, ARTICLE_UPDATED)
    search_fields = (ARTICLE_TEXT, ARTICLE_TITLE)
admin.site.register(Article, ArticleAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (SUBJECT_NAME, SUBJECT_SHOW)
admin.site.register(Subject, SubjectAdmin)


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('__str__', 'show', 'important', 'created', 'updated')
    search_fields = ('text', 'title')
admin.site.register(News, NewsAdmin)

class ResultsAdmin(admin.ModelAdmin):
    # Копипаста из NewsAdmin
    form = NewsForm
    list_display = ('__str__', 'show', 'important', 'created', 'updated')
    search_fields = ('text', 'title')
admin.site.register(Results, ResultsAdmin)

class PartnerEventAdmin(admin.ModelAdmin):
    form = PartnerEventAdminForm
    readonly_fields = ('created', 'updated',)
    list_display = ('title', 'date', 'show', 'partner', 'created', 'updated',)
admin.site.register(PartnerEvent, PartnerEventAdmin)


class PartnerEventInlineAdmin(admin.StackedInline):
    extra = 0
    model = PartnerEvent
    form = PartnerEventAdminForm
    classes = ['collapse']


class PartnerAdmin(admin.ModelAdmin):
    inlines = [PartnerEventInlineAdmin]
    list_display = ('name', 'show')
    readonly_fields = ('image_thumb',)
admin.site.register(Partner, PartnerAdmin)
