from django import forms

from articles.article_constants import NEWS_TITLE, NEWS_TEXT, NEWS_CREATED, NEWS_SHOW, \
    NEWS_IMPORTANT, NEWS_Y_POS, NEWS_AUTHOR, NEWS_KEY_TITLE_HELP_TEXT, NEWS_KEY_TEXT_HELP_TEXT, \
    NEWS_KEY_CREATED_HELP_TEXT, NEWS_KEY_SHOW_HELP_TEXT, NEWS_KEY_IMPORTANT_HELP_TEXT, NEWS_KEY_Y_POS_HELP_TEXT, \
    NEWS_KEY_AUTHOR_HELP_TEXT
from articles.models import News


class NewsForm(forms.ModelForm):
    model = News
    fields = (
        NEWS_TITLE,
        NEWS_TEXT,
        NEWS_CREATED,
        NEWS_SHOW,
        NEWS_IMPORTANT,
        NEWS_Y_POS,
        NEWS_AUTHOR,
    )

    help_text = {
        NEWS_TITLE: NEWS_KEY_TITLE_HELP_TEXT,
        NEWS_TEXT: NEWS_KEY_TEXT_HELP_TEXT,
        NEWS_CREATED: NEWS_KEY_CREATED_HELP_TEXT,
        NEWS_SHOW: NEWS_KEY_SHOW_HELP_TEXT,
        NEWS_IMPORTANT: NEWS_KEY_IMPORTANT_HELP_TEXT,
        NEWS_Y_POS: NEWS_KEY_Y_POS_HELP_TEXT,
        NEWS_AUTHOR: NEWS_KEY_AUTHOR_HELP_TEXT,
    }