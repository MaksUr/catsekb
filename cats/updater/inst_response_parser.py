from cats.updater.inst_request import get_first_photo_from_tag


def get_the_oldest_photo_descr_from_tag(tag, client):
    photo_response = get_first_photo_from_tag(tag, client)
    try:
        description = photo_response[-1]
    except IndexError:
        return None
    else:
        #############################################
        from os.path import join
        from os import mkdir
        from cats.updater.helper_functions import save_json
        try:
            mkdir(join('other', 'tags'))
        except FileExistsError:
            pass
        save_json(join('other', 'tags', tag), photo_response)
        #############################################
        return description
