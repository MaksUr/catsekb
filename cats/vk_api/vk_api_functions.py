import json
from os.path import abspath

import requests

RESPONSE = "response"
TITLE = "title"
TEXT = "text"
ITEMS = "items"
PID = "pid"
CREATED = "created"
SIZES = "sizes"
TYPE = "type"
SRC = "src"


def get_album(group_id, album_id):
    group_id = -1 * group_id
    photos = requests.get(r'https://api.vk.com/method/photos.get', params={
        'album_id': album_id,
        'owner_id': group_id,
        'photo_sizes': 1,
    }).json()
    return photos


def get_album_list(group_id):
    r = requests.get(r'https://api.vk.com/method/photos.getAlbums', params={
        'owner_id': -1 * group_id,
    }).json()
    return r


def save_json(file_name, data):
    file_name = abspath(file_name)
    with open(file_name + '.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print('create file:', file_name)
