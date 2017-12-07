import json
from os.path import join, abspath

from cats.cats_constants import VK_GROUP_ID, ANIMAL_VK_ALBUM_ID, ANIMAL_VALID_INFO
from cats.models import Animal
from cats.update_scripts.vk_response_parser import get_animal_kwargs_from_vk_response
from cats.updater import get_albums_info, RESPONSE, AID, TITLE, update_images_for_animal

KEY_IGNORE_TITLES = 'ignore_albums_titles'


def print_log(*args, **kwargs):
    from sys import stdout
    try:
        log_file = kwargs.pop('log_file')
    except KeyError:
        kwargs['file'] = stdout
    else:
        kwargs['file'] = log_file
    print(*args, **kwargs)


def check_end_file_name(f_name, suffix):
    """

    :type suffix: str
    :type f_name: str
    """
    if f_name.endswith(suffix):
        return f_name
    else:
        return f_name + suffix


def open_json(file_name, log_file=None):
    file_name = check_end_file_name(file_name, '.json')
    try:
        res = json.load(open(file_name, 'r', encoding="utf-8"))
    except FileNotFoundError:
        f = abspath(file_name)
        message = 'Файл:\n\t{f}\n\t - не найден\n\t{n}'.format(f=f, n=file_name)
        print_log(message, log_file=log_file)
        raise ValueError(message)
    else:
        print_log('open file:', file_name, log_file=log_file)
        return res


def update_all_animals_from_vk(conf_pth=None):
    if conf_pth is None:
        conf_pth = join(join('cats', 'update_scripts', 'config.json'))
    try:
        albums = get_albums_info(group_id=VK_GROUP_ID, album_ids=None)[RESPONSE]
    except KeyError:
        return None
    try:
        config = open_json(conf_pth)
        ignore_titles = config[KEY_IGNORE_TITLES]
    except (ValueError, KeyError, IndexError):
        ignore_titles = ()

    for item in albums:
        aid = item.get(AID)
        if (
                (item.get(TITLE) in ignore_titles) or (aid is None)
        ):
            continue

        animal, created = Animal.objects.get_or_create(**{ANIMAL_VK_ALBUM_ID: aid})
        if animal.__getattribute__(ANIMAL_VALID_INFO) is True:
            continue
        if created:
            c = 'Создан'
        else:
            c = 'Обновлен'
        print('{c} "{a}"'.format(c=c, a=animal))
        kwargs = get_animal_kwargs_from_vk_response({RESPONSE: (item,)})
        for k in kwargs:
            animal.__setattr__(k, kwargs[k])
        try:
            animal.save(update_fields=kwargs.keys())
        except (KeyError, ValueError, TypeError):
            pass
        update_images_for_animal(animal, aid)
        print('finish')
