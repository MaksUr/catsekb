from cats.constants import ANIMAL_DESCRIPTION, ANIMAL_NAME


def get_vk_album_id_from_url(url):
    # TODO: implement
    if url:
        return 666
    else:
        return None


def get_vk_url_from_album_id(album_id):
    # TODO: implement
    if album_id:
        return 'http://vk.com/album/{alb_id}'.format(alb_id=album_id)
    else:
        return 'http://vk.com/album/{alb_id}'.format(alb_id=1)


def update_animal_name_from_vk_album(animal):
    # TODO: implement
    #
    # if animal.vk_album_id is not None:
    #     return {'name': 'test__test'}
    #     pass
    # else:
    #     return dict()
    return {ANIMAL_NAME: 'test__test'}


def update_animal_descr_from_vk_album(animal):
    # TODO: implement
    #
    # if animal.vk_album_id is not None:
    #     return {'name': 'test__test'}
    #     pass
    # else:
    #     return dict()
    return {ANIMAL_DESCRIPTION: 'test__test'}
