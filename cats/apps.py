from django.apps import AppConfig

from cats.constants import APPLICATION_VERBOSE_NAME


class CatsConfig(AppConfig):
    name = 'cats'
    verbose_name = APPLICATION_VERBOSE_NAME
