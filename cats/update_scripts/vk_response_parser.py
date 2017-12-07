from cats.cats_constants import ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX, ANIMAL_DESCRIPTION
from cats.update_scripts.descr_analyzer import get_info_from_description
from cats.update_scripts.name_analyzer import get_info_from_title, get_sex
from cats.updater import TITLE, RESPONSE, DESCRIPTION, CREATED

NAME_DATA_KEYS = (ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX)


def get_description(description):
    if description:
        return description.replace('<br>', '')
    else:
        return None


def get_kwargs_from_album_response_title(vk_albums_response):
    status = None
    sex = None
    name = None
    try:
        title = vk_albums_response[RESPONSE][0][TITLE]
    except (KeyError, IndexError):
        title = None
    if title:
        status, name = get_info_from_title(title)
        sex = get_sex(title)
    res = {key: val for key, val in zip(NAME_DATA_KEYS, (name, status, sex)) if val}
    return res


def get_kwargs_from_album_response_descr(vk_albums_response):
    res = dict()
    try:
        vk_descr = vk_albums_response[RESPONSE][0][DESCRIPTION]
    except (KeyError, IndexError):
        vk_descr = None

    try:
        created_stamp = vk_albums_response[RESPONSE][0][CREATED]
    except (KeyError, IndexError):
        created_stamp = None

    description = get_description(vk_descr)
    if description:
        res.update(get_info_from_description(description, created_stamp))
        res[ANIMAL_DESCRIPTION] = description
    return res


def get_animal_kwargs_from_vk_response(vk_albums_response):
    res = dict()
    # name, location_status, sex
    res.update(get_kwargs_from_album_response_title(vk_albums_response=vk_albums_response))
    # description tag date_of_birth birthday_precision field_value
    res.update(
        get_kwargs_from_album_response_descr(
            vk_albums_response=vk_albums_response,
        )
    )
    return res
