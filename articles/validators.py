from django.core.exceptions import ValidationError

from articles.article_constants import ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE, ARTICLES_DEFAULT_CAPTIONS


def article_name_validator(title):
    if title in ARTICLES_DEFAULT_CAPTIONS:
        message = ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE.format(title=title)
        raise ValidationError(message)
