from django.core.exceptions import ValidationError

from articles.article_constants import ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE

DEFAULT_ARTICLE_NAMES = ()


def article_name_validator(title):
    if title in DEFAULT_ARTICLE_NAMES:
        message = ARTICLE_TITLE_VALIDATION_HAS_DEFAULT_VALUE.format(title=title)
        raise ValidationError(message)
