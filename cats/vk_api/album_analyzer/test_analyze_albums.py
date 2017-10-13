from cats.vk_api.album_analyzer.analyze_albums import get_name_status, STATUS_HOME, STATUS_SHELTER, STATUS_DIE
from cats.vk_api.helper_functions import replace_str_end_at_empty


# TODO : create tests


def check_name_result(a, b):
    if a != b:
        print('Ошибка! "{a}" не равно - "{b}" '.format(a=a, b=b))


def checks_name_analyzer_home():

    name = "ПРИСТРОЕН Шкода"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Шкода'))

    name = "ПРИСТРОЕН Кроули"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Кроули'))

    name = "Орхидея ПРИСТРОЕНА"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Орхидея'))

    name = "ПРИСТРОЕНЫ Зефир, Крем, Сливка, Трюфелька"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Зефир, Крем, Сливка, Трюфелька'))

    name = "Пристроен_Аль КОТоне"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Аль КОТоне'))

    name = "ПРИСТРОЕНА_Мона"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Мона'))

    name = "ПРИСТРОЕН_Бритый Кот"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Бритый Кот'))

    name = "Грю_ПРИСТРОЕН"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Грю'))

    name = "Тимми - ПРИСТРОЕН"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Тимми'))

    name = "ПРИСТРОЕНЫ сфинксы Смайл и Ксавьер"
    check_name_result(get_name_status(name), (STATUS_HOME, 'сфинксы Смайл и Ксавьер'))

    name = "ПРИСТРОЕНА Клеопатра (бывшая Клюшка)"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Клеопатра (бывшая Клюшка)'))

    name = "Пристроен Джанго"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Джанго'))

    name = "Масечка пристроен!"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Масечка'))

    name = "Нарцисс пристроен!"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Нарцисс'))

    name = "Пристроена! суслик"
    check_name_result(get_name_status(name), (STATUS_HOME, 'суслик '))

    name = "Тимми - ПРИСТРОЕН"
    check_name_result(get_name_status(name), (STATUS_HOME, 'Тимми'))


def checks_name_analyzer_shelter():

    name = "ИСПЫТАЛКА Оливка"
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'ИСПЫТАЛКА Оливка'))

    name = "Котюня"
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'Котюня'))

    name = "Дон Батон"
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'Дон Батон'))

    name = "Фрау Мяу"
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'Фрау Мяу'))

    name = "Котюня "
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'Котюня'))

    name = "Котюня_ "
    check_name_result(get_name_status(name), (STATUS_SHELTER, 'Котюня'))


def checks_name_analyzer_die():
    name = "НА РАДУГЕ Эльза"
    check_name_result(get_name_status(name), (STATUS_DIE, 'Эльза'))

    name = "НА РАДУГЕ Рокфор"
    check_name_result(get_name_status(name), (STATUS_DIE, 'Рокфор'))


def check_parse_name_home_status():
    # TODO : do nothing
    pass


def check_parse_name_die_status():
    # TODO : do nothing
    pass


def check_parse_name():
    # TODO : do nothing
    pass


def check_change_name():
    name = "  Фрау Мяу_"
    compare = "Фрау Мяу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = " Мяу   "
    compare = "Мяу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = "-___Фрау Мяу   "
    compare = "Фрау Мяу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = "- Фрау Мяу "
    compare = "Фрау Мяу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = "____Фрау Мяу "
    compare = "Фрау Мяу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = ",,,Зефир, Крем, Сливка, Трюфелька    "
    compare = "Зефир, Крем, Сливка, Трюфелька"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = "Сливка"
    compare = "Сливка"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = 'Лас кюня '
    compare = "Лас кюня"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = '_dsалв ана    '
    compare = "dsалв ана"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = 'аывае нвыавапыа  '
    compare = "аывае нвыавапыа"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = '_____вапыв апыупыаывимывапнкфуыапывпsd+++++'
    compare = "вапыв апыупыаывимывапнкфуыапывпsd"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = '__2312ывапыцук епуыап ывапфыу   ___---'
    compare = "2312ывапыцук епуыап ывапфыу"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = '   фыв апцй укпак---'
    compare = "фыв апцй укпак"
    check_name_result(replace_str_end_at_empty(name), compare)

    name = 'ф ыцфепцу'
    compare = "ф ыцфепцу"
    check_name_result(replace_str_end_at_empty(name), compare)


def main_all_test():
    checks_name_analyzer_home()
    checks_name_analyzer_shelter()
    checks_name_analyzer_die()
    check_parse_name_home_status()
    check_parse_name_die_status()
    check_parse_name()
    check_change_name()


if __name__ == '__main__':
    main_all_test()
