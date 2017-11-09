def get_vk_album_id_from_url(url):
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