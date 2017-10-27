from os.path import join
from urllib.request import pathname2url

from cats.constants import ANIMAL_NAME, ANIMAL_SEX, ANIMAL_DESCRIPTION, ANIMAL_LOCATION_STATUS
from cats.models import Animal, AnimalImage
from cats.vk_api.helper_functions import open_json, print_log

# http://127.0.0.1:8000/media/images/cats/albums/Багира/photos/246566509_456241041.jpg

CONFIG = r'cats\vk_api\album_analyzer\parse_album_list.json'
ROOT_PTH = r'http://127.0.0.1:8000/'
START_IMAGE_PTH = join('media', 'images', 'cats')


def save_image(animal, image_url, alt='alt', width=0, height=0, favourite=False, log_file=None):
    image_url = join(START_IMAGE_PTH, image_url)
    image_url = pathname2url(image_url)
    image_url = ROOT_PTH + image_url
    ai = AnimalImage(
        animal=animal,
        image_url=image_url,
        alt=alt,
        width=width,
        height=height,
        favourite=favourite
    )
    ai.save()
    print_log('save image', animal, log_file=log_file)


def save_images(animal, images, log_file=None):
    for image_pth in images:
        save_image(animal=animal, image_url=image_pth, log_file=log_file)


def get_images_info(local_ph, info):
    pass  # TODO: implement


def save_animal(animal_d, log_file=None):
    kwargs = dict()
    kwargs[ANIMAL_NAME] = animal_d[ANIMAL_NAME]
    kwargs[ANIMAL_LOCATION_STATUS] = animal_d[ANIMAL_LOCATION_STATUS]
    if animal_d.get(ANIMAL_SEX) is not None:
        kwargs[ANIMAL_SEX] = animal_d[ANIMAL_SEX]
    if animal_d.get(ANIMAL_DESCRIPTION):
        kwargs[ANIMAL_DESCRIPTION] = animal_d[ANIMAL_DESCRIPTION]
    animal = Animal(**kwargs)
    animal.save()
    images = animal_d['local_photos']
    images_info = get_images_info(local_ph=images, info=animal_d['vk_photos'])

    print_log('save', animal, log_file=log_file)
    save_images(animal=animal, images=images, log_file=log_file)


def save_animal_from_config(conf_pth=CONFIG, log_file=None):
    c = open_json(conf_pth)
    for animal in c:
        save_animal(animal, log_file=log_file)

if __name__ == '__main__':
    l = [
        "albums\\Дон Батон\\photos\\247143964_456241175.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241176.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241177.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241178.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241179.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241180.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241182.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241184.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241185.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241186.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241187.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241188.jpg",
        "albums\\Дон Батон\\photos\\247143964_456241209.jpg"
    ]
    info = [
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c836527/v836527682/7767f/cEur55gCRr0.jpg"
                },
                "aid": 247143964,
                "pid": 456241175,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622721,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c836527/v836527682/77689/uI6zJwT6-lc.jpg"
                },
                "aid": 247143964,
                "pid": 456241176,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622724,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 1703,
                    "width": 2560,
                    "src": "https://pp.userapi.com/c836527/v836527682/77693/JB8kBzhNfOQ.jpg"
                },
                "aid": 247143964,
                "pid": 456241177,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622727,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1438,
                    "src": "https://pp.userapi.com/c836527/v836527682/7769d/Qe5Lg0XNxIA.jpg"
                },
                "aid": 247143964,
                "pid": 456241178,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622730,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1438,
                    "src": "https://pp.userapi.com/c836527/v836527682/776a7/ssciRS9PzcM.jpg"
                },
                "aid": 247143964,
                "pid": 456241179,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622733,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c836527/v836527682/776b1/1usS2Q_BEGY.jpg"
                },
                "aid": 247143964,
                "pid": 456241180,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622735,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c836527/v836527682/776c5/aO9hM6A3reQ.jpg"
                },
                "aid": 247143964,
                "pid": 456241182,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622739,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c836527/v836527682/776d9/2dNly_-Kjfc.jpg"
                },
                "aid": 247143964,
                "pid": 456241184,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622742,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 1703,
                    "width": 2560,
                    "src": "https://pp.userapi.com/c836527/v836527682/776e3/lOgUTjpI0jY.jpg"
                },
                "aid": 247143964,
                "pid": 456241185,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622744,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 1707,
                    "width": 2560,
                    "src": "https://pp.userapi.com/c836527/v836527682/776ed/0A8eSAmG4gc.jpg"
                },
                "aid": 247143964,
                "pid": 456241186,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622750,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1440,
                    "src": "https://pp.userapi.com/c836527/v836527682/776f7/zcoTbCXAHfs.jpg"
                },
                "aid": 247143964,
                "pid": 456241187,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622754,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 1707,
                    "width": 2560,
                    "src": "https://pp.userapi.com/c836527/v836527682/77701/kBvSTtp4jNE.jpg"
                },
                "aid": 247143964,
                "pid": 456241188,
                "text": "",
                "owner_id": -73666865,
                "created": 1504622760,
                "user_id": 100
            },
            {
                "vk_src": {
                    "type": "w",
                    "height": 2160,
                    "width": 1437,
                    "src": "https://pp.userapi.com/c837532/v837532393/59ae6/WDUkA2Vi5aY.jpg"
                },
                "aid": 247143964,
                "pid": 456241209,
                "text": "",
                "owner_id": -73666865,
                "created": 1504839981,
                "user_id": 100
            }
        ]
    # get_images_info(local_ph=l, info=info)

    # save_animal_from_config()
