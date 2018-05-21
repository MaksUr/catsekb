import datetime
try:
    import requests
except ImportError:
    requests = None

from cats.cats_constants import ANIMAL_IMAGE_PHOTO_ID, ANIMAL_IMAGE_ANIMAL, ANIMAL_IMAGE_IMAGE_URL, \
    ANIMAL_IMAGE_IMAGE_SMALL_URL, ANIMAL_IMAGE_CREATED, ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND
from catsekb.constants import VK_GROUP_ID, CREATED
from catsekb.settings import VK_TOKEN
from cats.models import AnimalImage

RESPONSE = "response"
ITEMS = "items"
PID = "pid"
SIZES = "sizes"
TYPE = "type"
SRC = "src"
AID = "aid"

SIZE_TYPES = ("w", "z", "y", "r", "x", "q", "p", "o", "m", "s",)
SMALL_SIZE_TYPE = "r"
BIG_SIZE_TYPE = "w"
API_VERSION = "5.64"


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


def get_album_photos_local(album_id):
    from urllib.request import pathname2url
    from os.path import join, dirname
    from os import listdir
    from cats.update_scripts.all_update import open_json

    def get_local_image_url(image_url):
        image_url = pathname2url(image_url)
        image_url = r'http://127.0.0.1:8000/' + image_url
        return image_url

    photos_config_file = r'media\images\cats\albums\{aid}\{aid}.json'.format(aid=album_id)
    try:
        photos = open_json(photos_config_file)
    except ValueError:
        return {'response': ()}
    photos = {'response': photos}
    local_photo_dir = join(dirname(photos_config_file), 'photos')
    file_names = listdir(local_photo_dir)
    for photo_d, file_name in zip(photos['response'], file_names):
        for photo_link in photo_d['sizes']:
            photo_link['src'] = get_local_image_url(join(local_photo_dir, file_name))
    return photos


def get_album_photos(group_id, album_id):
    if requests is not None:
        group_id = -1 * group_id
        r = requests.get(r'https://api.vk.com/method/photos.get', params={
            'album_id': album_id,
            'owner_id': group_id,
            'photo_sizes': 1,
            'v': API_VERSION,
            'access_token': VK_TOKEN,
        })
        photos = r.json()        
    else:
        photos = get_album_photos_local(album_id)
    return photos


def get_albums_info_local(album_ids):
    from cats.update_scripts.all_update import open_json
    r = open_json(r'other\albums.json')
    if album_ids:
        l = r['response']
        l = filter((lambda x: x['aid'] in album_ids), l)
        l = filter((lambda x: x['aid'] in album_ids), l)
        r['response'] = list(l)
    return r


def get_albums_info(group_id, album_ids):
    if requests is not None:
        params = dict()
        params['owner_id'] = -1 * group_id
        if album_ids:
            params['album_ids'] = ','.join(map(str, album_ids))
        r = requests.get(r'https://api.vk.com/method/photos.getAlbums', params={
            'owner_id': -1 * group_id,
            'v': API_VERSION,
        }).json()
    else:
        r = get_albums_info_local(album_ids)
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
    pid = photo.get('id')
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
        images = get_album_photos(VK_GROUP_ID, album_id)[RESPONSE]['items']
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



