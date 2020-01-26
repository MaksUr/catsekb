from django.apps import AppConfig


class CatsConfig(AppConfig):
    # TODO: Переименовать cats в pets
    # Содержит сущность "Питомец"
    name = 'cats'
    verbose_name = 'Питомцы'
