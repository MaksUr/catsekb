from django.core.exceptions import ValidationError

from cats.constants import ANIMAL_LOCATION_STATUS_CHOICE_HOME, ANIMAL_LOCATION_STATUS_CHOICE_SHELTER, \
    ANIMAL_LOCATION_STATUS_CHOICE_DEAD, GROUP_ALL_ANIMALS_KEY_NAME, GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT

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