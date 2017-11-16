from os.path import join
from urllib.request import pathname2url

from cats.constants import VK_GROUP_ID
from cats.vk_api import vk_api_functions
from cats.vk_api.album_analyzer.analyze_albums import SIZES
from cats.vk_api.name_analyzer import analyse_animal_name
from cats.vk_api.vk_api_functions import TITLE, TEXT, ITEMS, PID, CREATED, TYPE, SRC


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
    name = response.get(TITLE)
    if name:
        name = analyse_animal_name(name)
    return name


def get_animal_descr_from_vk_response(response):
    album_descr = response.get(TEXT)
    # TODO: implement
    return 'test__description' + str(album_descr)


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




def save_image(photo):
    pid = photo.get(PID)
    created = photo.get(CREATED)
    photos = photo.get(SIZES, ())
    biggest_photo = get_photo_from_size(photos, biggest=False)
    small_photo = get_photo_from_size(photos, biggest=False)
    # TODO: save image


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
    for photo in response.get(ITEMS, ()):
        save_image(photo)


