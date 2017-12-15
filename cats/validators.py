from django.core.exceptions import ValidationError

from cats.cats_constants import GROUP_INSTANCE_SHELTER_NAME, GROUP_INSTANCE_DEAD_NAME, \
    GROUP_INSTANCE_ALL_NAME, GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT, ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS, \
    GROUP_INSTANCE_HOME_NAME

DEFAULT_GROUP_NAMES = (
    GROUP_INSTANCE_HOME_NAME,
    GROUP_INSTANCE_SHELTER_NAME,
    GROUP_INSTANCE_DEAD_NAME,
    GROUP_INSTANCE_ALL_NAME,
)


def group_name_validator(name):
    if name in DEFAULT_GROUP_NAMES:
        message = GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT.format(name=name)
        raise ValidationError(message)


def background_y_position_validator(value):
    if value > 100 or value < 0:
        message = ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS.format(val=value)
        raise ValidationError(message)

