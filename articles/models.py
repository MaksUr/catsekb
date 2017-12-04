from django.db import models

# Create your models here.
from django.db.models import Model, CharField, TextField, DateTimeField, BooleanField, ForeignKey

from articles.article_constants import ARTICLE_KEY_TITLE, ARTICLE_KEY_TEXT, ARTICLE_KEY_CREATED, ARTICLE_KEY_UPDATED, \
    ARTICLE_KEY_SHOW, AUTHOR_KEY_NAME, ARTICLE_VERBOSE_NAME, ARTICLE_VERBOSE_NAME_PLURAL, AUTHOR_VERBOSE_NAME, \
    AUTHOR_VERBOSE_NAME_PLURAL
from articles.validators import article_name_validator


class Author(Model):
    name = CharField(AUTHOR_KEY_NAME, max_length=120, unique=True)

    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME
        verbose_name_plural = AUTHOR_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name


class Article(Model):
    title = CharField(ARTICLE_KEY_TITLE, max_length=70, unique=True, validators=[article_name_validator])
    text = TextField(ARTICLE_KEY_TEXT, default='')
    created = DateTimeField(ARTICLE_KEY_CREATED, auto_now_add=True)
    updated = DateTimeField(ARTICLE_KEY_UPDATED, auto_now=True)
    show = BooleanField(ARTICLE_KEY_SHOW, default=True)
    author = ForeignKey(Author, verbose_name=Author._meta.verbose_name)

    class Meta:
        verbose_name = ARTICLE_VERBOSE_NAME
        verbose_name_plural = ARTICLE_VERBOSE_NAME_PLURAL

    def __str__(self):
        return '{title}: {text}...'.format(title=self.title, text=self.text[:15])
