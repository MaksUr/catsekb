from django import forms
from django.core.exceptions import ValidationError

from articles.article_constants import NEWS_TITLE, NEWS_TEXT, NEWS_SHOW, \
    NEWS_IMPORTANT, NEWS_Y_POS, NEWS_AUTHOR, NEWS_KEY_TITLE_HELP_TEXT, NEWS_KEY_TEXT_HELP_TEXT, \
    NEWS_KEY_SHOW_HELP_TEXT, NEWS_KEY_IMPORTANT_HELP_TEXT, NEWS_KEY_Y_POS_HELP_TEXT, \
    NEWS_KEY_AUTHOR_HELP_TEXT, ARTICLE_TITLE, ARTICLE_TEXT, ARTICLE_SHOW, ARTICLE_AUTHOR, \
    ARTICLE_SUBJECT, ARTICLE_Y_POS, ARTICLE_USE_BACKGROUND, ARTICLE_KEY_TITLE_HELP_TEXT, ARTICLE_KEY_TEXT_HELP_TEXT, \
    ARTICLE_KEY_SHOW_HELP_TEXT, ARTICLE_KEY_AUTHOR_HELP_TEXT, \
    ARTICLE_KEY_SUBJECT_HELP_TEXT, ARTICLE_KEY_Y_POS_HELP_TEXT, ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE, \
    ARTICLES_DEFAULT_MAPPING
from articles.models import News, Article
from catsekb.constants import IMAGE, IMAGE_KEY_HELP_TEXT


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            NEWS_TITLE,
            NEWS_TEXT,
            NEWS_SHOW,
            NEWS_IMPORTANT,
            NEWS_Y_POS,
            NEWS_AUTHOR,
        )

        help_texts = {
            NEWS_TITLE: NEWS_KEY_TITLE_HELP_TEXT,
            NEWS_TEXT: NEWS_KEY_TEXT_HELP_TEXT,
            NEWS_SHOW: NEWS_KEY_SHOW_HELP_TEXT,
            NEWS_IMPORTANT: NEWS_KEY_IMPORTANT_HELP_TEXT,
            NEWS_Y_POS: NEWS_KEY_Y_POS_HELP_TEXT,
            NEWS_AUTHOR: NEWS_KEY_AUTHOR_HELP_TEXT,
            IMAGE: IMAGE_KEY_HELP_TEXT,
        }


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            ARTICLE_TITLE,
            ARTICLE_TEXT,
            ARTICLE_SHOW,
            ARTICLE_AUTHOR,
            ARTICLE_SUBJECT,
            IMAGE,
            ARTICLE_Y_POS,
            ARTICLE_USE_BACKGROUND,
        )

        help_texts = {
            ARTICLE_TITLE: ARTICLE_KEY_TITLE_HELP_TEXT,
            ARTICLE_TEXT: ARTICLE_KEY_TEXT_HELP_TEXT,
            ARTICLE_SHOW: ARTICLE_KEY_SHOW_HELP_TEXT,
            ARTICLE_AUTHOR: ARTICLE_KEY_AUTHOR_HELP_TEXT,
            ARTICLE_SUBJECT: ARTICLE_KEY_SUBJECT_HELP_TEXT,
            IMAGE: IMAGE_KEY_HELP_TEXT,
            ARTICLE_Y_POS: ARTICLE_KEY_Y_POS_HELP_TEXT,
            ARTICLE_USE_BACKGROUND: ARTICLE_KEY_Y_POS_HELP_TEXT,
        }

    def clean_title(self):
        if self.instance.id in ARTICLES_DEFAULT_MAPPING and ARTICLE_TITLE in self.changed_data:
            message = ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE.format(title=self.instance.title)
            raise ValidationError(message)
        return self.cleaned_data[ARTICLE_TITLE]

