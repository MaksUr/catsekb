# import requests TODO: import
from os import listdir
from os.path import join, dirname
from urllib.request import pathname2url


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


def get_album_photos(group_id, album_id):
    # group_id = -1 * group_id
    # TODO: use requests
    # photos = requests.get(r'https://api.vk.com/method/photos.get', params={
    #     'album_id': album_id,
    #     'owner_id': group_id,
    #     'photo_sizes': 1,
    # }).json()

    ###############################################
    # TODO: локальная заглушка
    from cats.updater.helper_functions import open_json
    def get_local_image_url(image_url):
        image_url = pathname2url(image_url)
        image_url = r'http://127.0.0.1:8000/' + image_url
        return image_url

    photos_config_file = r'media\images\cats\albums\{title}\{aid}.json'.format(title=album_id[1], aid=album_id[0])
    photos = open_json(photos_config_file)
    photos = {'response': photos}
    local_photo_dir = join(dirname(photos_config_file), 'photos')
    file_names = listdir(local_photo_dir)
    for photo_d, file_name in zip(photos['response'], file_names):
        for photo_link in photo_d['sizes']:
            photo_link['src'] = get_local_image_url(join(local_photo_dir, file_name))
    ###############################################

    return photos


def get_albums_info(group_id, album_ids):
    # params = dict()

    # params['owner_id'] = -1 * group_id
    # if album_ids:
    #     params['album_ids'] = ','.join(map(str, album_ids))
    # TODO: use requests
    # r = requests.get(r'https://api.vk.com/method/photos.getAlbums', params={
    #     'owner_id': -1 * group_id,
    # }).json()

    ###############################################
    # TODO: локальная заглушка
    from cats.updater.helper_functions import open_json
    r = open_json(r'other\albums.json')
    ###############################################

    return r
