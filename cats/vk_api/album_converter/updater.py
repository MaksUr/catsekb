import datetime
from os.path import join

from django.core.exceptions import ObjectDoesNotExist

from cats.constants import VK_GROUP_ID, ANIMAL_NAME, ANIMAL_DESCRIPTION, ANIMAL_LOCATION_STATUS, ANIMAL_SEX, \
    ANIMAL_SHELTER_DATE
from cats.models import Animal
from cats.vk_api.helper_functions import open_json
from cats.vk_api.vk_api_functions import get_album_photos, get_albums_info
from cats.vk_api.vk_import import get_animal_name_from_vk_response, get_animal_descr_from_vk_response, \
    add_images_from_response


def save_animal(data):
    response = {
        'response': [
            data
        ]
    }
    name_data = get_animal_name_from_vk_response(response=response)
    descr = get_animal_descr_from_vk_response(response=response)
    kwargs = dict()
    kwargs.update(name_data)
    if descr:
        kwargs[ANIMAL_DESCRIPTION] = descr
    kwargs[ANIMAL_SHELTER_DATE] = datetime.date.fromtimestamp(int(data['created']))
    # TODO: group
    kwargs['vk_album_id'] = data["aid"]
    animal = Animal(**kwargs)
    animal.save()
    # photo_response = get_album_photos(group_id=data["owner_id"], album_id=data["aid"])

    ########################################
    # TODO: локальная заглушка
    try:
        photo_response = get_album_photos(group_id=data["owner_id"], album_id=(data["aid"], data["title"]))
    except ValueError:
        return
    ########################################

    add_images_from_response(animal=animal, response=photo_response)


def update_all_animals_from_response(response):
    """
    Добавляет Animal по полю vk_album_id
    :param response: 
    :type response: 
    :return: 
    :rtype: 
    """
    config = open_json(join('cats', 'vk_api', 'album_analyzer', 'config.json'))
    ignore_list = config['settings']['ignore_albums']
    try:
        albums = response['response']
    except KeyError:
        return
    for animal in albums:
        if animal.get('title') in ignore_list:
            continue
        try:
            Animal.objects.get(vk_album_id=animal["aid"])
        except (Animal.MultipleObjectsReturned,):
            m = 'Одинаковые vk_album_id={aid} у разных экземпляров.'.format(aid=animal["aid"])
            raise Exception(m)
        except ObjectDoesNotExist:
            save_animal(data=animal)
    else:
        print('finish')


def update_all_animals():
    response = get_albums_info(album_ids=None, group_id=VK_GROUP_ID)
    update_all_animals_from_response(response=response)




