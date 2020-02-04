from django.core.exceptions import ValidationError

from cats.cats_constants import GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT, \
    ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS

DEFAULT_GROUP_NAMES = (
    'Пристроены',
    'Ищут дом',
    'На радуге',
    'Все котики',
)


def group_name_validator(name):
    if name in DEFAULT_GROUP_NAMES:
        message = GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT.format(name=name)
        raise ValidationError(message)


def background_y_position_validator(value):
    if value > 100 or value < 0:
        message = ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS.format(val=value)
        raise ValidationError(message)

