from cats.constants import ANIMAL_SEX, ANIMAL_LOCATION_STATUS, \
    ANIMAL_NAME, ANIMAL_TAG, ANIMAL_DESCRIPTION, ANIMAL_DATE_OF_BIRTH, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_FIELD_VALUE, \
    HASHTAG_TEMPLATE, HASHTAG_SUFFIX
from cats.updater.descr_analyzer import get_animal_tag, get_info_from_description
from cats.updater.inst_response_parser import get_the_oldest_photo_descr_from_tag
from cats.updater.name_analyzer import get_info_from_title, get_sex
from cats.updater.vk_request import RESPONSE, TITLE, DESCRIPTION, TYPE, SRC, CREATED

NAME_DATA_KEYS = (ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX)


def get_description(client, title=None, vk_descr=None, name=None):
    if name:
        tag = HASHTAG_TEMPLATE.format(name=name, suffix=HASHTAG_SUFFIX)
        description = get_the_oldest_photo_descr_from_tag(tag, client=client)
        if description:
            return description

    if title:
        title_name = get_info_from_title(title)[1]
        if title_name:
            tag = HASHTAG_TEMPLATE.format(name=title_name, suffix=HASHTAG_SUFFIX)
            description = get_the_oldest_photo_descr_from_tag(tag, client=client)
            if description:
                return description

    if vk_descr:
        tag = get_animal_tag(vk_descr)
        if tag:
            description = get_the_oldest_photo_descr_from_tag(tag, client=client)
            if description:
                return description
        else:
            res = vk_descr.replace('<br>', '')
            return res

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


def get_kwargs_from_album_response_descr(vk_albums_response, client, name=None):
    res = dict()
    try:
        vk_descr = vk_albums_response[RESPONSE][0][DESCRIPTION]
    except (KeyError, IndexError):
        vk_descr = None

    try:
        created_stamp = vk_albums_response[RESPONSE][0][CREATED]
    except (KeyError, IndexError):
        created_stamp = None

    try:
        title = vk_albums_response[RESPONSE][0][TITLE]
    except (KeyError, IndexError):
        title = None

    description = get_description(title=title, vk_descr=vk_descr, name=name, client=client)
    if description:
        res.update(get_info_from_description(description, created_stamp))
        res[ANIMAL_DESCRIPTION] = description
    return res


def get_animal_kwargs_from_vk_response(vk_albums_response, client):
    res = dict()

    res.update(get_kwargs_from_album_response_title(vk_albums_response=vk_albums_response)) # name, location_status, sex
    name = res.get(ANIMAL_NAME)
    res.update(
        get_kwargs_from_album_response_descr(
            vk_albums_response=vk_albums_response,
            name=name,
            client=client
        )
    )
    return res


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


# TODO: get_image_args
