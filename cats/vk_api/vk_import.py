import datetime
from os.path import join
from urllib.request import pathname2url

from cats.constants import VK_GROUP_ID, ANIMAL_IMAGE_IMAGE_URL, ANIMAL_IMAGE_IMAGE_SMALL_URL, ANIMAL_IMAGE_PHOTO_ID, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_CREATED
from cats.vk_api import vk_api_functions
from cats.vk_api.album_analyzer.analyze_albums import SIZES
from cats.vk_api.name_analyzer import analyse_animal_name
from cats.vk_api.vk_api_functions import TITLE, TEXT, ITEMS, PID, CREATED, TYPE, SRC, RESPONSE


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


def get_vk_url_from_album_id(album_id):
    if album_id:
        return r"https://vk.com/album-{group_id}_{album_id}".format(group_id=VK_GROUP_ID, album_id=album_id)
    else:
        return None


def get_animal_name_from_vk_response(response):
    if not response.get(RESPONSE):
        return None
    name = response[RESPONSE].get(TITLE)
    if name:
        name = analyse_animal_name(name)[1]
    return name


def get_animal_descr_from_vk_response(response):
    if not response.get(RESPONSE):
        return None
    album_descr = response[RESPONSE].get(TEXT)
    if album_descr is None:
        return None
    else:
        return album_descr


SIZE_TYPES = ("w", "z", "y", "r", "x", "q", "p", "o", "m", "s",)
SMALL_SIZE_TYPE = "r"
BIG_SIZE_TYPE = "w"


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
    # TODO: implement
    ###############################
    # p = join('media', 'test_images')
    # photos = (
    #     ('1.jpg', 1),
    #     ('2.jpg', 2),
    #     ('NPOA_logo_st_pos_cmyk.jpg', 3),
    #     ('на листе.jpg', 4),
    #     ('ракета_логотипы.jpg', 5),
    #     ('ракета_логотипы_priv.jpg', 6),
    #     ('1.jpg', 7)
    # )
    # for image_url, photo_id in photos:
    #     image_url = join(p, image_url)
    #     image_url = pathname2url(image_url)
    #     image_url = r'http://127.0.0.1:8000/' + image_url
    #     animal.add_animal_image(image_url=image_url, photo_id=photo_id)
    ###############################
    response = response.get(RESPONSE)
    if response is None:
        return response
    photos = iter(response.get(ITEMS, ()))
    try:
        save_image(animal=animal, photo=next(photos), background=True)
        save_image(animal=animal, photo=next(photos), favourite=True)
    except StopIteration:
        return
    for photo in photos:
        save_image(animal=animal, photo=photo)



