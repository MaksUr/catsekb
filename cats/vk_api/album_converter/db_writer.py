from cats.constants import ANIMAL_NAME, ANIMAL_SEX, ANIMAL_DESCRIPTION, ANIMAL_LOCATION_STATUS
from cats.models import Animal, AnimalImage
from cats.vk_api.helper_functions import open_json, print_log

CONFIG = r'C:\rep\djangoProjects\cekb\cats\vk_api\album_analyzer\parse_album_list.json'


def save_image(animal, image_url, alt='alt', width=0, height=0, favourite=False, log_file=None):
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
    for i in images:
        save_image(animal=animal, image_url=i, log_file=log_file)
        break


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
    print_log('save', animal, log_file=log_file)
    save_images(animal=animal, images=images, log_file=log_file)


def save_animal_from_config(conf_pth, log_file=None):
    c = open_json(conf_pth)
    for animal in c:
        save_animal(animal, log_file=log_file)
        break

# if __name__ == '__main__':
#     save_animal_from_config()
