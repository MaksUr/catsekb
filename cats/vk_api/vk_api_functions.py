import json
from os.path import abspath

# import requests TODO: import
from cats.vk_api.helper_functions import open_json

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


def get_album_photos(group_id, album_id):
    group_id = -1 * group_id
    # TODO: use requests
    # photos = requests.get(r'https://api.vk.com/method/photos.get', params={
    #     'album_id': album_id,
    #     'owner_id': group_id,
    #     'photo_sizes': 1,
    # }).json()
    ###############################################
    photos = open_json(r'other\album_example.json')
    ###############################################
    return photos


def get_albums_info(group_id, album_ids):
    params = dict()
    params['owner_id'] = -1 * group_id
    if album_ids:
        params['album_ids'] = ','.join(map(str, album_ids))
    # TODO: use requests
    # r = requests.get(r'https://api.vk.com/method/photos.getAlbums', params={
    #     'owner_id': -1 * group_id,
    # }).json()
    ###############################################
    r = open_json(r'other\albums.json')
    ###############################################
    return r
