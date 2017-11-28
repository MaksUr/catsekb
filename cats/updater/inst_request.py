

def get_first_photo_from_tag(tag, client, limit=10):
    # # TODO: get response example
    # photo_response = {
    #     'response': {'description': 'описание'}
    # }
    if tag.startswith('#'):
        t = tag[1:]
    else:
        t = tag
    photo_response = client.search_by_tag(t, limit=limit)

    return photo_response

