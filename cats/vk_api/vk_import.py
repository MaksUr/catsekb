from os.path import join
from urllib.request import pathname2url

from cats.constants import ANIMAL_DESCRIPTION, ANIMAL_NAME, VK_GROUP_ID


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


def get_animal_name_from_vk_album(vk_album):
    # TODO: implement
    return 'test__name_' + str(vk_album)


def get_animal_descr_from_vk_album(vk_album):
    # TODO: implement
    return 'test__description' + str(vk_album)


def add_images_from_album(animal):
    if animal.vk_album_id is None:
        return
    # TODO: implement
    res = True
    ###############################

    p = join('media', 'test_images')
    photos = (
        ('1.jpg', 1),
        ('2.jpg', 2),
        ('NPOA_logo_st_pos_cmyk.jpg', 3),
        ('на листе.jpg', 4),
        ('ракета_логотипы.jpg', 5),
        ('ракета_логотипы_priv.jpg', 6),
        ('1.jpg', 7)
    )
    for image_url, photo_id in photos:
        image_url = join(p, image_url)
        image_url = pathname2url(image_url)
        image_url = r'http://127.0.0.1:8000/' + image_url
        status = animal.add_animal_image(image_url=image_url, photo_id=photo_id)
        if not status:
            return False
    else:
        return res
    ###############################


