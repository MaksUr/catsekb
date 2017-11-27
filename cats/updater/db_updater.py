import datetime

from cats.constants import ANIMAL_VK_ALBUM_ID, VK_GROUP_ID, ANIMAL_FIELD_VALUE, FIELD_TYPE_NAME, FIELD_VALUE_VALUE_TEXT, \
    FIELD_VALUE_FIELD_TYPE, ANIMAL_IMAGE_IMAGE_URL, ANIMAL_IMAGE_IMAGE_SMALL_URL, ANIMAL_IMAGE_PHOTO_ID, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_CREATED, ANIMAL_IMAGE_ANIMAL
from cats.models import Animal, FieldType, FieldValue, AnimalImage
from cats.updater.helper_functions import open_json
from cats.updater.vk_request import get_albums_info, RESPONSE, TITLE, AID, get_album_photos, PID, CREATED, SIZES
from cats.updater.vk_response_parser import get_animal_kwargs_from_vk_response, get_photo_from_size

KEY_IGNORE_TITLES = 'ignore_albums_titles'


def set_field_values_to_animal(animal, field_values):
    for field_type in field_values:
        kwargs = {FIELD_TYPE_NAME: field_type}
        field_type_instance, created= FieldType.objects.get_or_create(**kwargs)
        kwargs = {
            FIELD_VALUE_VALUE_TEXT: field_values[field_type],
            FIELD_VALUE_FIELD_TYPE: field_type_instance
        }
        field_value, created = FieldValue.objects.get_or_create(**kwargs)
        animal.field_value.add(field_value)


def save_image(animal, photo, favourite=False, background=False):
    photos = photo.get(SIZES, ())
    biggest_photo = get_photo_from_size(photos, biggest=True)
    small_photo = get_photo_from_size(photos, biggest=False)
    pid = photo.get(PID)
    created = photo.get(CREATED)
    if created is not None:
        created = datetime.datetime.fromtimestamp(created).date()

    kwargs = dict()
    kwargs[ANIMAL_IMAGE_PHOTO_ID] = pid
    kwargs[ANIMAL_IMAGE_ANIMAL] = animal
    image = AnimalImage.objects.get_or_create(**kwargs)
    if biggest_photo:
        image.__setattr__(ANIMAL_IMAGE_IMAGE_URL, biggest_photo)
    if small_photo:
        image.__setattr__(ANIMAL_IMAGE_IMAGE_SMALL_URL, small_photo)
    if created:
        image.__setattr__(ANIMAL_IMAGE_CREATED, created)

    image.__setattr__(ANIMAL_IMAGE_FAVOURITE, favourite)
    image.__setattr__(ANIMAL_IMAGE_BACKGROUND, background)


def update_images_for_animal(animal, album_id):
    try:
        images = get_album_photos(VK_GROUP_ID, album_id)[RESPONSE]
    except KeyError:
        return None
    try:
        images = iter(images)
    except TypeError:
        return None
    try:
        save_image(animal=animal, photo=next(images), background=True)
        save_image(animal=animal, photo=next(images), favourite=True)
    except StopIteration:
        return
    for image in images:
        save_image(animal=animal, photo=image)


def update_all_animals_from_vk(conf_pth='config.json'):
    try:
        albums = get_albums_info(group_id=VK_GROUP_ID, album_ids=None)[RESPONSE]
    except KeyError:
        return None
    try:
        config = open_json(conf_pth)
        ignore_titles = config[KEY_IGNORE_TITLES]
    except (ValueError, KeyError, IndexError):
        ignore_titles = ()

    for item in albums:
        aid = item.get(AID)
        if (
                (item.get(TITLE) in ignore_titles) or (aid is None)
        ):
            continue

        animal, created = Animal.objects.get_or_create(**{ANIMAL_VK_ALBUM_ID: aid})

        kwargs = get_animal_kwargs_from_vk_response({RESPONSE: (item,)})
        field_values = kwargs.pop(ANIMAL_FIELD_VALUE, dict())
        set_field_values_to_animal(animal, field_values)
        update_images_for_animal(animal, aid)










