from django.core.exceptions import ValidationError

from cats.constants import ANIMAL_LOCATION_STATUS_CHOICE_HOME, ANIMAL_LOCATION_STATUS_CHOICE_SHELTER, \
    ANIMAL_LOCATION_STATUS_CHOICE_DEAD, GROUP_ALL_ANIMALS_KEY_NAME, GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT, \
    ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS

DEFAULT_GROUP_NAMES = (
    ANIMAL_LOCATION_STATUS_CHOICE_HOME,
    ANIMAL_LOCATION_STATUS_CHOICE_SHELTER,
    ANIMAL_LOCATION_STATUS_CHOICE_DEAD,
    GROUP_ALL_ANIMALS_KEY_NAME,
)


def group_name_validator(name):
    if name in DEFAULT_GROUP_NAMES:
        message = GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT.format(name=name)
        raise ValidationError(message)


def background_y_position_validator(value):
    if 0 > value > 100:
        message = ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS.format(val=value)
        raise ValidationError(message)

