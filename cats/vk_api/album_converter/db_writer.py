from cats.constants import ANIMAL_NAME, ANIMAL_SEX, ANIMAL_DESCRIPTION, ANIMAL_LOCATION_STATUS
from cats.models import Animal
from cats.vk_api.helper_functions import open_json, print_log

CONFIG = r'C:\rep\djangoProjects\cekb\cats\vk_api\album_analyzer\parse_album_list.json'


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
    print_log('save', animal, log_file=log_file)


def save_animal_from_config(conf_pth, log_file=None):
    c = open_json(conf_pth)
    for animal in c:
        save_animal(animal, log_file=log_file)

# if __name__ == '__main__':
#     save_animal_from_config()
