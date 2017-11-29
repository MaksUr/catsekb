import datetime

import requests

from cats.constants import ANIMAL_IMAGE_PHOTO_ID, ANIMAL_IMAGE_ANIMAL, ANIMAL_IMAGE_IMAGE_URL, \
    ANIMAL_IMAGE_IMAGE_SMALL_URL, ANIMAL_IMAGE_CREATED, ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, VK_GROUP_ID
from cats.models import AnimalImage

RESPONSE = "response"
TITLE = "title"
TEXT = "text"
ITEMS = "items"
PID = "pid"
CREATED = "created"
SIZES = "sizes"
TYPE = "type"
SRC = "src"
DESCRIPTION = "description"
AID = "aid"

SIZE_TYPES = ("w", "z", "y", "r", "x", "q", "p", "o", "m", "s",)
SMALL_SIZE_TYPE = "r"
BIG_SIZE_TYPE = "w"


def get_vk_album_id_from_url(url):
    group = "album-" + str(VK_GROUP_ID) + "_"
    if url and r'vk.com/' in url and url.find(group) >= 0:
        album_id = url[url.find(group) + len(group):]
        try:
            album_id = int(album_id)
        except ValueError:
            return None
        else:
            return album_id
    else:
        return None


def get_album_photos(group_id, album_id):
    group_id = -1 * group_id
    # TODO: use requests
    photos = requests.get(r'https://api.vk.com/method/photos.get', params={
        'album_id': album_id,
        'owner_id': group_id,
        'photo_sizes': 1,
    }).json()

    return photos


def get_albums_info(group_id, album_ids):
    params = dict()

    params['owner_id'] = -1 * group_id
    if album_ids:
        params['album_ids'] = ','.join(map(str, album_ids))
    # TODO: use requests
    r = requests.get(r'https://api.vk.com/method/photos.getAlbums', params={
        'owner_id': -1 * group_id,
    }).json()

    return r


def get_photo_from_size(list_size, biggest=True):
    if biggest:
        start_index = SIZE_TYPES.index(BIG_SIZE_TYPE)
    else:
        start_index = SIZE_TYPES.index(SMALL_SIZE_TYPE)

    for size_type in SIZE_TYPES[start_index:]:
        for photo in list_size:
            if photo.get(TYPE) == size_type:
                return photo.get(SRC)
    else:
        return None


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
    image, c = AnimalImage.objects.get_or_create(**kwargs)
    if biggest_photo:
        image.__setattr__(ANIMAL_IMAGE_IMAGE_URL, biggest_photo)
    if small_photo:
        image.__setattr__(ANIMAL_IMAGE_IMAGE_SMALL_URL, small_photo)
    if created:
        image.__setattr__(ANIMAL_IMAGE_CREATED, created)
    if c:
        image.__setattr__(ANIMAL_IMAGE_FAVOURITE, favourite)
        image.__setattr__(ANIMAL_IMAGE_BACKGROUND, background)
    image.save()


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



