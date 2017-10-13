import re

from os.path import join

from cats.constants import ANIMAL_LOCATION_STATUS_DEAD, ANIMAL_LOCATION_STATUS_SHELTER, ANIMAL_LOCATION_STATUS_HOME, \
    ANIMAL_SEX_MALE, ANIMAL_SEX_FEMALE, ANIMAL_LOCATION_STATUS, ANIMAL_NAME, ANIMAL_SEX
from cats.vk_api.helper_functions import save_json, open_json, replace_str_end_at_empty, print_log

SIZES = 'sizes'

VK_PHOTOS = 'vk_photos'

PARSE_ALBUM_LIST = 'parse_album_list'

VK_SRC = 'vk_src'

LOCAL_PHOTOS = 'local_photos'

CONFIG_SETTINGS = 'settings'
CONFIG_SETTINGS_IGNORE_ALBUMS = 'ignore_albums'
CONFIG_SETTINGS_ALBUMS_TITLES = 'albums_titles'

PRINTING = False

LABEL = 'label'
PATTERN = 'pattern'

CONFIG_FILE_NAME = 'config.json'

STATUS_HOME = ANIMAL_LOCATION_STATUS_HOME
STATUS_DIE = ANIMAL_LOCATION_STATUS_DEAD
STATUS_SHELTER = ANIMAL_LOCATION_STATUS_SHELTER

PATTERN_SEX_M = re.compile(r"ПРИСТРОЕН(?!А)", flags=re.IGNORECASE)
PATTERN_SEX_F = re.compile(r"ПРИСТРОЕНА", flags=re.IGNORECASE)

MAPPING = {
    STATUS_HOME: {
        LABEL: 'ПРИСТРОЕН',
        PATTERN: re.compile(
            r"([ -]+)?(_)?(!)?ПРИСТРОЕН(А|Ы)?(_)?(!)?( +)?",
            flags=re.IGNORECASE
        ),
    },
    STATUS_DIE: {
        LABEL: 'НА РАДУГЕ',
        PATTERN: re.compile(
            r"_?НА РАДУГЕ_?([ ]+)?",
            flags=re.IGNORECASE
        )
    },
    STATUS_SHELTER: {
        LABEL: 'В ПРИЮТЕ',
        PATTERN: None
    },
}


def get_sex(title):
    if re.search(PATTERN_SEX_M, title) is not None:
        return ANIMAL_SEX_MALE
    elif re.search(PATTERN_SEX_F, title) is not None:
        return ANIMAL_SEX_FEMALE
    else:
        return None


def collect_albums_to_file(log_file=None):
    print_log('='*20, log_file=log_file)
    print_log('collect_albums_to_file', log_file=log_file)
    config = open_json(CONFIG_FILE_NAME, log_file=log_file)
    for s in config[CONFIG_SETTINGS_ALBUMS_TITLES]:
        print_log(s, log_file=log_file)


def get_albums_titles(titles, albums_config_file, log_file=None):
    albums = open_json(albums_config_file)
    res = list()
    for a in albums:
        res.append(a['title'])
    save_json(titles, res, log_file=log_file)
    return res


def check_name_status(name, status, log_file=None):
    res = None
    pattern = MAPPING[status][PATTERN]
    if pattern is None:
        res = name
    else:
        m = re.search(pattern, name)
        if m is not None:
            match = m.group()
            r = name.replace(match, "")
            res = r or None

    if res is not None:
        res = replace_str_end_at_empty(res, log_file=log_file)
        print_log(
            'alb_title-"{t}"\n\tname-"{r}"\n\tstatus-"{s}"'.format(
                r=res,
                t=name,
                s=status
            ),
            log_file=log_file
        )
    # else:
    #     print_log('alb_title-"{n}" - None'.format(n=name), log_file=log_file)
    return res


def get_name_status(name, log_file=None):
    r = check_name_status(name, STATUS_HOME, log_file=log_file)
    if r is not None:
        return STATUS_HOME, r
    else:
        r = check_name_status(name, STATUS_DIE, log_file=log_file)
        if r is not None:
            return STATUS_DIE, r
        else:
            r = check_name_status(name, STATUS_SHELTER, log_file=log_file)
            if r is None:
                message = 'Для имени {n} - статус не найден'.format(n=name)
                print_log(message)
                raise ValueError(message)
            return STATUS_SHELTER, r


def get_biggest_photo(sizes_list):
    biggest = sizes_list[0]
    for size in sizes_list:
        if size['width'] > biggest['width']:
            biggest = size
    return biggest


def parse_album_item_vk_photo(photo, log_file=None):
    photo[VK_SRC] = get_biggest_photo(photo[SIZES])
    del photo[SIZES]
    return photo


def parse_album_item_vk_photos(photos, log_file=None):
    res = list()
    for p in photos:
        res.append(parse_album_item_vk_photo(photo=p, log_file=log_file))
    return res


def parse_album_item(alb, log_file=None):
    start_local_pth = ''  # TODO: Выяснить путь в джанго
    alb[LOCAL_PHOTOS] = [join(start_local_pth, p) for p in alb[LOCAL_PHOTOS]]
    alb[ANIMAL_LOCATION_STATUS], alb[ANIMAL_NAME] = get_name_status(alb['title'], log_file=log_file)
    alb[VK_PHOTOS] = parse_album_item_vk_photos(alb[VK_PHOTOS], log_file=log_file)
    alb[ANIMAL_SEX] = get_sex(alb['title'])
    return alb


def parse_album_list(log_file=None):

    album_list_pth = r'album_list_detailed_local.json'
    album_list = open_json(album_list_pth, log_file=log_file)
    config = open_json(CONFIG_FILE_NAME, log_file=log_file)
    ignore_list = config[CONFIG_SETTINGS][CONFIG_SETTINGS_IGNORE_ALBUMS]
    res = list()
    for alb in album_list:

        if alb['title'] in ignore_list:
            print_log('ignore album:', alb['title'], log_file=log_file)
            continue
        else:
            res.append(parse_album_item(alb=alb, log_file=log_file))
    return res


def save_parse_album_list():
    with open('log.txt', 'w', encoding='UTF-8') as log:
        alb_l = parse_album_list(log_file=log)
        save_json(file_name=PARSE_ALBUM_LIST, data=alb_l, log_file=log)


def main():
    pass


if __name__ == '__main__':
    save_parse_album_list()
