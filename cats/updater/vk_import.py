import datetime

from cats.constants import VK_GROUP_ID, ANIMAL_IMAGE_IMAGE_URL, ANIMAL_IMAGE_IMAGE_SMALL_URL, ANIMAL_IMAGE_PHOTO_ID, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_CREATED, ANIMAL_SEX, ANIMAL_LOCATION_STATUS, \
    ANIMAL_NAME, ANIMAL_TAG, ANIMAL_DESCRIPTION, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE

from cats.updater.descr_analyzer import get_info_from_description
from cats.updater.name_analyzer import get_info_from_title, get_sex
from cats.updater.vk_request import TITLE, PID, CREATED, TYPE, SRC, RESPONSE, DESCRIPTION, SIZES

# NAME_DATA_KEYS = (ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX)
# DESCR_DATA_KEYS = (ANIMAL_DESCRIPTION, ANIMAL_TAG, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE)


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


def get_vk_url_from_album_id(album_id, group_id=VK_GROUP_ID):
    if album_id:
        return r"https://vk.com/album-{group_id}_{album_id}".format(group_id=group_id, album_id=album_id)
    else:
        return None


# def get_animal_name_from_vk_response(response):
#     status = None
#     sex = None
#     name = None
#     try:
#         title = response[RESPONSE][0][TITLE]
#     except (KeyError, IndexError):
#         title = None
#     if title:
#         status, name = get_info_from_title(title)
#         sex = get_sex(title)
#     res = {key: val for key, val in zip(NAME_DATA_KEYS, (name, status, sex)) if val}
#     return res


# def get_animal_descr_from_vk_response(response):
#     album_descr = None
#     res = dict()
#     try:
#         album_descr = response[RESPONSE][0][DESCRIPTION]
#     except (KeyError, IndexError):
#         pass
#     else:
#         album_descr = album_descr.replace('<br>', '')
#
#     if album_descr:
#         res.update(get_info_from_description(album_descr))
#         res[ANIMAL_DESCRIPTION] = album_descr
#
#
#     # TODO: extra info
#     # TODO: tag +
#     # TODO: age +
#     return res


# SIZE_TYPES = ("w", "z", "y", "r", "x", "q", "p", "o", "m", "s",)
# SMALL_SIZE_TYPE = "r"
# BIG_SIZE_TYPE = "w"
#
#
# def get_photo_from_size(list_size, biggest=True):
#     if biggest:
#         start_index = SIZE_TYPES.index(BIG_SIZE_TYPE)
#     else:
#         start_index = SIZE_TYPES.index(SMALL_SIZE_TYPE)
#
#     for size_type in SIZE_TYPES[start_index:]:
#         for photo in list_size:
#             if photo.get(TYPE) == size_type:
#                 return photo.get(SRC)
#     else:
#         return None


def save_image(animal, photo, favourite=False, background=False):
    photos = photo.get(SIZES, ())
    biggest_photo = get_photo_from_size(photos, biggest=True)
    small_photo = get_photo_from_size(photos, biggest=False)
    pid = photo.get(PID)
    created = photo.get(CREATED)
    if created is not None:
        created = datetime.datetime.fromtimestamp(created)

    kwargs = dict()
    kwargs[ANIMAL_IMAGE_IMAGE_URL] = biggest_photo
    kwargs[ANIMAL_IMAGE_IMAGE_SMALL_URL] = small_photo
    kwargs[ANIMAL_IMAGE_PHOTO_ID] = pid
    kwargs[ANIMAL_IMAGE_FAVOURITE] = favourite
    kwargs[ANIMAL_IMAGE_BACKGROUND] = background
    kwargs[ANIMAL_IMAGE_CREATED] = created.date()

    animal.add_animal_image(**kwargs)


def add_images_from_response(animal, response):
    photos = response.get(RESPONSE)
    if photos is None:
        return photos
    try:
        photos = iter(photos)
    except TypeError:
        return
    try:
        save_image(animal=animal, photo=next(photos), background=True)
        save_image(animal=animal, photo=next(photos), favourite=True)
    except StopIteration:
        return
    for photo in photos:
        save_image(animal=animal, photo=photo)



