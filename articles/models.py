import re
from django.db.models import Model, CharField, TextField, DateTimeField, BooleanField, ForeignKey, QuerySet, \
    IntegerField, URLField, CASCADE
from django.urls import reverse
from ckeditor.fields import RichTextField

from articles.article_constants import ARTICLE_KEY_TITLE, ARTICLE_KEY_TEXT, ARTICLE_KEY_CREATED, ARTICLE_KEY_UPDATED, \
    ARTICLE_KEY_SHOW, AUTHOR_KEY_NAME, ARTICLE_VERBOSE_NAME, ARTICLE_VERBOSE_NAME_PLURAL, AUTHOR_VERBOSE_NAME, \
    AUTHOR_VERBOSE_NAME_PLURAL, SUBJECT_KEY_NAME, SUBJECT_VERBOSE_NAME, SUBJECT_VERBOSE_NAME_PLURAL, \
    ARTICLES_DEFAULT_MAPPING, URL, SUBJECT_KEY_SHOW, NEWS_VERBOSE_NAME, NEWS_VERBOSE_NAME_PLURAL, NEWS_KEY_TITLE, \
    NEWS_KEY_TEXT, NEWS_KEY_CREATED, NEWS_KEY_UPDATED, NEWS_KEY_SHOW, NEWS_KEY_Y_POS, NEWS_KEY_IMPORTANT, \
    NEWS_USE_BACKGROUND, ARTICLE_KEY_Y_POS, ARTICLE_USE_BACKGROUND, NEWS_KEY_USE_BACKGROUND, ARTICLE_KEY_USE_BACKGROUND
from articles.validators import article_name_validator
from cats.validators import background_y_position_validator
from catsekb.constants import DJ_PK, URL_NAME_SUBJECT, URL_NAME_ARTICLE, URL_NAME_POST, IMAGE_KEY

SEARCH_TAG_PATTERN = re.compile(r'<.+?>', re.S)


class Author(Model):
    name = CharField(AUTHOR_KEY_NAME, max_length=120, unique=True)

    class Meta:
        verbose_name = AUTHOR_VERBOSE_NAME
        verbose_name_plural = AUTHOR_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name


class Subject(Model):
    name = CharField(SUBJECT_KEY_NAME, max_length=120, unique=True)
    show = BooleanField(SUBJECT_KEY_SHOW, default=True)

    class Meta:
        verbose_name = SUBJECT_VERBOSE_NAME
        verbose_name_plural = SUBJECT_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(URL_NAME_SUBJECT, kwargs={DJ_PK: self.id})


class Article(Model):
    title = CharField(ARTICLE_KEY_TITLE, max_length=70, unique=True)
    text = RichTextField(ARTICLE_KEY_TEXT)
    created = DateTimeField(ARTICLE_KEY_CREATED, auto_now_add=True)
    updated = DateTimeField(ARTICLE_KEY_UPDATED, auto_now=True)
    show = BooleanField(ARTICLE_KEY_SHOW, default=True)
    author = ForeignKey(Author, on_delete=CASCADE, verbose_name=Author._meta.verbose_name, null=True, blank=True)
    subject = ForeignKey(Subject, on_delete=CASCADE, verbose_name=Subject._meta.verbose_name, null=True, blank=True)
    image = URLField(IMAGE_KEY, null=True, blank=True, default=None)
    y_pos = IntegerField(ARTICLE_KEY_Y_POS, blank=True, default=50, validators=[background_y_position_validator])
    use_background = BooleanField(ARTICLE_KEY_USE_BACKGROUND, default=True)

    class Meta:
        verbose_name = ARTICLE_VERBOSE_NAME
        verbose_name_plural = ARTICLE_VERBOSE_NAME_PLURAL

    def __str__(self):
        return '{title}: {text}...'.format(title=self.title or 'Статья', text=self.text[:15])

    def get_absolute_url(self):
        if ARTICLES_DEFAULT_MAPPING.get(self.id) is not None:
            return reverse(ARTICLES_DEFAULT_MAPPING[self.id][URL])
        else:
            return reverse(URL_NAME_ARTICLE, kwargs={DJ_PK: self.id})

    def get_background_style(self):
        if self.image and self.use_background:
            res = 'background-image: url({url}); background-size: cover; background-position-y: {ypos}%;'.format(
                url=self.image, ypos=self.y_pos
            )
        else:
            res = None
        return res


class News(Model):
    title = CharField(NEWS_KEY_TITLE, max_length=70)
    text = RichTextField(NEWS_KEY_TEXT)
    created = DateTimeField(NEWS_KEY_CREATED, auto_now_add=True)
    updated = DateTimeField(NEWS_KEY_UPDATED, auto_now=True)
    show = BooleanField(NEWS_KEY_SHOW, default=True)
    author = ForeignKey(Author, on_delete=CASCADE, verbose_name=Author._meta.verbose_name, null=True, blank=True)
    image = URLField(IMAGE_KEY, null=True, blank=True, default=None)
    important = BooleanField(NEWS_KEY_IMPORTANT, default=False)
    y_pos = IntegerField(NEWS_KEY_Y_POS, blank=True, default=50, validators=[background_y_position_validator])
    use_background = BooleanField(NEWS_KEY_USE_BACKGROUND, default=True)

    class Meta:
        verbose_name = NEWS_VERBOSE_NAME
        verbose_name_plural = NEWS_VERBOSE_NAME_PLURAL

    def __str__(self):
        return '{title}: {text}...'.format(title=self.title or 'Новость', text=self.text[:15])

    def get_absolute_url(self):
        return reverse(URL_NAME_POST, kwargs={DJ_PK: self.id})

    def get_background_style(self):
        if self.image and self.use_background:
            res = 'background-image: url({url}); background-size: cover; background-position-y: {ypos}%;'.format(
                url=self.image, ypos=self.y_pos
            )
        else:
            res = None
        return res
