from os.path import join
from urllib.request import pathname2url

from cats.constants import ANIMAL_NAME, ANIMAL_SEX, ANIMAL_DESCRIPTION, ANIMAL_LOCATION_STATUS
from cats.models import Animal, AnimalImage
from cats.vk_api.helper_functions import open_json, print_log

# http://127.0.0.1:8000/media/images/cats/albums/Багира/photos/246566509_456241041.jpg

CONFIG = join('cats', 'vk_api', 'album_analyzer', 'parse_album_list.json')
ROOT_PTH = r'http://127.0.0.1:8000/'
START_IMAGE_PTH = join('media', 'images', 'cats')


def save_vk_image(
    animal,
    image,
    favourite,
    background,
    log_file=None
):
    image_url = image['vk_src']['src']
    width = image['vk_src']['width']
    height = image['vk_src']['height']
    ai = AnimalImage(
        animal=animal,
        image_url=image_url,
        width=width,
        height=height,
        favourite=favourite,
        background=background
    )
    ai.save()
    print_log('save image', animal, log_file=log_file)


def save_image(animal, image_info, favourite, background, log_file=None):
    image_url, info = image_info
    width, height = info
    image_url = get_local_image_url(image_url)
    ai = AnimalImage(
        animal=animal,
        image_url=image_url,
        favourite=favourite,
        background=background,
        width=width,
        height=height
    )
    ai.save()
    print_log('save image', animal, log_file=log_file)


def get_local_image_url(image_url):
    image_url = join(START_IMAGE_PTH, image_url)
    image_url = pathname2url(image_url)
    image_url = ROOT_PTH + image_url
    return image_url


def save_images(animal, images, use_local_photos, log_file=None):
    images = iter(images)
    if use_local_photos:
        try:
            image_pth = next(images)
            save_image(animal=animal, image_info=image_pth, log_file=log_file, favourite=False, background=True)

            image_pth = next(images)
            save_image(animal=animal, image_info=image_pth, log_file=log_file, favourite=True, background=False)

        except StopIteration:
            return
        for image_pth in images:
            save_image(animal=animal, image_info=image_pth, log_file=log_file, favourite=False, background=True)

    else:
        try:
            image = next(images)
            save_vk_image(animal=animal, image=image, log_file=log_file, favourite=False, background=True)

            image = next(images)
            save_vk_image(animal=animal, image=image, log_file=log_file, favourite=True, background=False)
        except StopIteration:
            return

        for image in images:
            save_vk_image(animal=animal, image=image, log_file=log_file, favourite=False, background=False)


def get_images_info(vk_photos):
    res = list()
    for photo in vk_photos:
        width = photo['vk_src']['width']
        height = photo['vk_src']['height']
        item = (width, height)
        res.append(item)
    return res


def save_animal(animal_d, log_file=None, use_local_photos=True):
    kwargs = dict()
    kwargs[ANIMAL_NAME] = animal_d[ANIMAL_NAME]
    kwargs[ANIMAL_LOCATION_STATUS] = animal_d[ANIMAL_LOCATION_STATUS]
    if animal_d.get(ANIMAL_SEX) is not None:
        kwargs[ANIMAL_SEX] = animal_d[ANIMAL_SEX]
    if animal_d.get(ANIMAL_DESCRIPTION):
        kwargs[ANIMAL_DESCRIPTION] = animal_d[ANIMAL_DESCRIPTION]
    animal = Animal(**kwargs)
    animal.save()
    if use_local_photos:
        images = animal_d['local_photos']
        images_info = get_images_info(vk_photos=animal_d['vk_photos'])
        images = zip(images, images_info)
    else:
        images = animal_d['vk_photos']
    print_log('save', animal, log_file=log_file)
    save_images(animal=animal, images=images, log_file=log_file, use_local_photos=use_local_photos)


def save_animal_from_config(use_local_photos, conf_pth=CONFIG, log_file=None):
    c = open_json(conf_pth)
    for animal in c[35:36]:
        save_animal(animal, use_local_photos=use_local_photos, log_file=log_file)

if __name__ == '__main__':
    save_animal_from_config(use_local_photos=False)
