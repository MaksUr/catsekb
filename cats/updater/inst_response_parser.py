from cats.updater.inst_request import get_first_photo_from_tag


def get_the_oldest_photo_descr_from_tag(tag):
    photo_response = get_first_photo_from_tag(tag)
    try:
        description = photo_response['response']['description']
    except KeyError:
        return None
    else:
        return "Описание из inst"
