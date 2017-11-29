import json
from os.path import abspath

from cats.constants import ANIMAL_LOCATION_STATUS, ANIMAL_VK_ALBUM_ID, ANIMAL_TAG, ANIMAL_SEX, ANIMAL_DESCRIPTION, \
    ANIMAL_NAME
from cats.models import Animal

FIELDS = (
    ANIMAL_NAME,
    ANIMAL_DESCRIPTION,
    ANIMAL_SEX,
    ANIMAL_VK_ALBUM_ID,
    ANIMAL_LOCATION_STATUS,
)


def save_json(file_name, data):
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print('create file:', abspath(file_name))


def get_data_from_animals(animal):
    res = dict()
    for f in FIELDS:
        v = animal.__getattribute__(f)
        if not isinstance(v, int):
            res[f] = str(v)
        else:
            res[f] = v
    res[ANIMAL_TAG] = animal.get_instagram_link()
    res['description_url'] = ''
    return res


def bd_to_json():
    animals = Animal.objects.all()
    res = list()
    for animal in animals:
        res.append(get_data_from_animals(animal))
    save_json('animals_config.json', res)


