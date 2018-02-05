# KEY - это название поля у которого есть значение.
# TEMPLATE - это шаблон. Переменные вставляются внуть скобок: '{название_поля} - {значение_поля}'
#
# verbose_name - название модели, plural - множ. число.
# field_set - объединение полей (заголовок)
#
# ANIMAL - питомец
# GROUP - группа
#
# foreign_key служит для связи текущей модели с другой моделью. Например модель - AnimalImage,
# foreign_key: animal ссылается на модель Animal.
# Это значит поле animal в AnimalImage относится к определенному Animal
from catsekb.constants import SHOW, NAME, DESCRIPTION, VK_GROUP_ID, NO_CHOICE, CREATED_KEY, CREATED, UPDATED, \
    UPDATED_KEY, IMAGE_BACKGROUND, IMAGE_KEY_BACKGROUND, IMAGE_KEY_BACKGROUND_HELP_TEXT, KEY_Y_POS, KEY_Y_POS_HELP_TEXT

GALLERY_DEFAULT_ITEMS_COUNT = 9

APPLICATION_VERBOSE_NAME = 'Котики'  # Название приложения

# class AnimalImage
ANIMAL_IMAGE_VERBOSE_NAME_PLURAL = 'Фотографии'
ANIMAL_IMAGE_VERBOSE_NAME = 'Фотография'

# animal (foreign key for class Animal)
ANIMAL_IMAGE_ANIMAL = 'animal'
ANIMAL_IMAGE_KEY_ANIMAL = '_Животное'  # TODO: edit value
ANIMAL_IMAGE_KEY_ANIMAL_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_ANIMAL'

# image
ANIMAL_IMAGE_IMAGE = 'image'
ANIMAL_IMAGE_KEY_IMAGE = 'Изображение'
ANIMAL_IMAGE_KEY_IMAGE_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_IMAGE'

# image_url
ANIMAL_IMAGE_IMAGE_URL = 'image_url'
ANIMAL_IMAGE_IMAGE_URL_TAG = 'image_url_tag'
ANIMAL_IMAGE_KEY_IMAGE_URL = 'URL изображения'
ANIMAL_IMAGE_KEY_IMAGE_URL_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_IMAGE_URL'

# image_small_url
ANIMAL_IMAGE_IMAGE_SMALL_URL = 'image_small_url'
ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG = 'image_small_url_tag'
ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL = 'URL сжатого изображения'
ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL'

# photo_id
ANIMAL_IMAGE_PHOTO_ID = 'photo_id'
ANIMAL_IMAGE_KEY_PHOTO_ID = 'ID фотографии'
ANIMAL_IMAGE_KEY_PHOTO_ID_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_WIDTH'


# favourite TODO: грамматическая ошибка
ANIMAL_IMAGE_FAVOURITE = 'favourite'
ANIMAL_IMAGE_KEY_FAVOURITE = 'Избранное'
ANIMAL_IMAGE_KEY_FAVOURITE_HELP_TEXT = 'Основное изображение страницы с котом.'

# background
ANIMAL_IMAGE_BACKGROUND = IMAGE_BACKGROUND
ANIMAL_IMAGE_KEY_BACKGROUND = IMAGE_KEY_BACKGROUND
ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT = IMAGE_KEY_BACKGROUND_HELP_TEXT

# created
ANIMAL_IMAGE_CREATED = CREATED
ANIMAL_IMAGE_KEY_CREATED = CREATED_KEY
ANIMAL_IMAGE_KEY_CREATED_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_CREATED'

# background_y_position
ANIMAL_IMAGE_BACKGROUND_Y_POSITION = 'background_y_position'
ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION = KEY_Y_POS
ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT = KEY_Y_POS_HELP_TEXT

ANIMAL_IMAGE_VALIDATION_WRONG_Y_POS = '{val} имеет недопустимое значение. Значение должно быть от 0 до 100.'

# image_thumb
ANIMAL_IMAGE_IMAGE_THUMB = 'image_thumb'
ANIMAL_IMAGE_KEY_IMAGE_THUMB = 'Фото'
ANIMAL_IMAGE_KEY_IMAGE_THUMB_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_IMAGE_THUMB'


# class Animal
ANIMAL_VERBOSE_NAME_PLURAL = 'Питомцы'
ANIMAL_VERBOSE_NAME = 'Питомец'
ANIMAL_MAIN_FIELD_SET = 'Общая информация'
ANIMAL_VK_IMPORT_SET = 'Импорт данных из группы в VK'
ANIMAL_VIDEO_FIELD_SET = 'Видео'

# tag
ANIMAL_TAG_FIELD_SET = 'Настройка тега'

ANIMAL_TAG = 'tag'
ANIMAL_KEY_TAG = 'Тэг животного'
ANIMAL_KEY_TAG_HELP_TEXT = 'При заполнении этого поля, будет использоваться данный пользовательский тег. ' \
                           'Символ "#" и окончание "_catsekb" подставляется автоматически. Пример заполнения: "Смурфик"'

# tag display

ANIMAL_TAG_DISPLAY = 'tag_display'
ANIMAL_KEY_TAG_DISPLAY = 'Текущий тег'
ANIMAL_KEY_TAG_DISPLAY_HELP_TEXT = 'Для обновления необходимо сохранить. Убедитесь в корректности ссылки.'

HASHTAG_TEMPLATE_INSTAGRAM = 'https://www.instagram.com/explore/tags/{name}_{suffix}/'
HASHTAG_TEMPLATE = '#{name}_{suffix}'
HASHTAG_SUFFIX = 'catsekb'

# name
ANIMAL_NAME = 'name'
ANIMAL_KEY_NAME = 'Имя'
ANIMAL_KEY_NAME_HELP_TEXT = 'Введите только имя. Хэштэг генерируется автоматически'
ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST = '"{name}" уже существует'

# description
ANIMAL_DESCRIPTION = 'description'
ANIMAL_KEY_DESCRIPTION = 'Описание'
ANIMAL_KEY_DESCRIPTION_HELP_TEXT = '_help_text ANIMAL_DESCRIPTION_KEY_DESCRIPTION'

# vk_album_id
ANIMAL_VK_ALBUM_ID = 'vk_album_id'
ANIMAL_KEY_VK_ALBUM_ID = 'ID альбома в VK'
ANIMAL_KEY_VK_ALBUM_ID_HELP_TEXT = 'ID альбома в VK'

# vk_album_url
ANIMAL_VK_ALBUM_URL = 'vk_album_url'
ANIMAL_KEY_VK_ALBUM_URL = 'Ссылка на альбом в VK'
ANIMAL_KEY_VK_ALBUM_URL_HELP_TEXT = 'Для изменения необходмо сохранить.'
ANIMAL_VK_ALBUM_URL_WRONG_FORMAT = '''Ссылка имеет недопустимое значение. 
Пример: https://vk.com/album-{group_id}_12345'''.format(group_id=VK_GROUP_ID)
ANIMAL_VK_ALBUM_URL_IS_EMPTY = 'Необходимо заполнить поле "{VK_ALBUM_URL}"'.format(VK_ALBUM_URL=ANIMAL_KEY_VK_ALBUM_URL)


ANIMAL_FORM_VK_UPDATE_PHOTO = 'vk_update_photo'
ANIMAL_KEY_FORM_VK_UPDATE_PHOTO = 'Обновить фото'
ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT = 'Перед нажатием нужно сохранить ссылку на альбом. ' \
                                            'Фото добавляется автоматически.'


ANIMAL_FORM_VK_UPDATE_INFO = 'vk_update_info'
ANIMAL_KEY_FORM_VK_UPDATE_INFO = 'Обновить описание и имя кота. '
ANIMAL_KEY_FORM_VK_UPDATE_INFO_HELP_TEXT = 'Для изменения требуется сохранить. ' \
                                           '(При возмозжности обновится статус, пол, возраст, ' \
                                           'дата дата попадания в приют)'


# sex
ANIMAL_SEX = 'sex'
ANIMAL_KEY_SEX = 'Пол'
ANIMAL_KEY_SEX_HELP_TEXT = 'Выберите пол'

ANIMAL_SEX_FEMALE = "F"  # для хранения в БД
ANIMAL_SEX_MALE = "M"  # для хранения в БД
ANIMAL_SEX_CHOICE_FEMALE = "Женский"
ANIMAL_SEX_CHOICE_MALE = "Мужской"
ANIMAL_SEX_CHOICES = (
    NO_CHOICE,
    (ANIMAL_SEX_MALE, ANIMAL_SEX_CHOICE_MALE),
    (ANIMAL_SEX_FEMALE, ANIMAL_SEX_CHOICE_FEMALE)
)

ANIMAL_SEX_CHOICES_D = {
    ANIMAL_SEX_MALE: ANIMAL_SEX_CHOICE_MALE,
    ANIMAL_SEX_FEMALE: ANIMAL_SEX_CHOICE_FEMALE
}

# location_status
ANIMAL_LOCATION_STATUS = 'location_status'
ANIMAL_KEY_LOCATION_STATUS = 'Статус'
ANIMAL_KEY_LOCATION_STATUS_HELP_TEXT = '_help_text ANIMAL_KEY_LOCATION_STATUS'

ANIMAL_LOCATION_STATUS_HOME = 'H'    # для хранения в БД
ANIMAL_LOCATION_STATUS_SHELTER = 'S'    # для хранения в БД
ANIMAL_LOCATION_STATUS_DEAD = 'D'    # для хранения в БД
ANIMAL_LOCATION_STATUS_CHOICE_HOME = 'Пристроен'
ANIMAL_LOCATION_STATUS_CHOICE_SHELTER = 'В поиске дома'
ANIMAL_LOCATION_STATUS_CHOICE_DEAD = 'На радуге'

ANIMAL_LOCATION_STATUS_CHOICES = (
    NO_CHOICE,
    (ANIMAL_LOCATION_STATUS_HOME, ANIMAL_LOCATION_STATUS_CHOICE_HOME),
    (ANIMAL_LOCATION_STATUS_SHELTER, ANIMAL_LOCATION_STATUS_CHOICE_SHELTER),
    (ANIMAL_LOCATION_STATUS_DEAD, ANIMAL_LOCATION_STATUS_CHOICE_DEAD),
)
ANIMAL_LOCATION_STATUS_CHOICES_D = {
    ANIMAL_LOCATION_STATUS_HOME: ANIMAL_LOCATION_STATUS_CHOICE_HOME,
    ANIMAL_LOCATION_STATUS_SHELTER: ANIMAL_LOCATION_STATUS_CHOICE_SHELTER,
    ANIMAL_LOCATION_STATUS_DEAD: ANIMAL_LOCATION_STATUS_CHOICE_DEAD,
}

# birthday_precision.
# Точность. Устанавливается в соответствии задаными параметрами возраста.
# При установки date_of_birth устанавливается точность DAY
ANIMAL_BIRTHDAY_PRECISION = 'birthday_precision'

ANIMAL_BIRTHDAY_PRECISION_DAY_CHOICE = "до дня"
ANIMAL_BIRTHDAY_PRECISION_MONTH_CHOICE = "до месяца"
ANIMAL_BIRTHDAY_PRECISION_YEAR_CHOICE = "до года"
ANIMAL_BIRTHDAY_PRECISION_DAY = "D"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_MONTH = "M"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_YEAR = "Y"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_CHOICES = (
        (ANIMAL_BIRTHDAY_PRECISION_YEAR, ANIMAL_BIRTHDAY_PRECISION_YEAR_CHOICE),
        (ANIMAL_BIRTHDAY_PRECISION_MONTH, ANIMAL_BIRTHDAY_PRECISION_MONTH_CHOICE),
        (ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_DAY_CHOICE),
    )

# date_of_birth
ANIMAL_DATE_OF_BIRTH = 'date_of_birth'

# shelter_date
ANIMAL_SHELTER_DATE = 'shelter_date'
ANIMAL_KEY_SHELTER_DATE = 'В приюте'
ANIMAL_KEY_SHELTER_DATE_HELP_TEXT = 'Примерная дата попадания в приют'

# group
ANIMAL_GROUP = 'group'
ANIMAL_KEY_GROUP_HELP_TEXT = 'Назначить группу для питомца.'

# video
ANIMAL_VIDEO = 'video'
ANIMAL_KEY_VIDEO_HELP_TEXT = 'Видео на котором есть питомец'

# show
ANIMAL_SHOW = SHOW
ANIMAL_KEY_SHOW = 'Показывать котика'
ANIMAL_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть.'

# valid_info
ANIMAL_VALID_INFO = 'valid_info'
ANIMAL_KEY_VALID_INFO = 'Проверено'
ANIMAL_KEY_VALID_INFO_HELP_TEXT = 'Информация проверена вручную.'


# created
ANIMAL_CREATED = CREATED
ANIMAL_KEY_CREATED = CREATED_KEY
ANIMAL_KEY_CREATED_HELP_TEXT = ''

# updated
ANIMAL_UPDATED = UPDATED
ANIMAL_KEY_UPDATED = UPDATED_KEY
ANIMAL_KEY_UPDATED_HELP_TEXT = ''

# Возраст. Определяет date_of_birth в том случае, если date_of_birth не редактировался пользователем.
ANIMAL_AGE_FIELD_SET = 'Возраст котика'
# days (AnimalForm) - возраст
ANIMAL_DAYS = 'days'
ANIMAL_FORM_KEY_DAYS = 'Дней'
ANIMAL_KEY_DAYS_HELP_TEXT = 'Указывается точность до дня'

# months (AnimalForm) - возраст
ANIMAL_MONTHS = 'months'
ANIMAL_FORM_KEY_MONTHS = 'Месяцев'
ANIMAL_KEY_MONTHS_HELP_TEXT = 'Указывается точность до месяца'

# years (AnimalForm) - возраст
ANIMAL_YEARS = 'years'
ANIMAL_FORM_KEY_YEARS = 'Лет'
ANIMAL_KEY_YEARS_HELP_TEXT = 'Указывается точность до года'


# class AnimalVideo
ANIMAL_VIDEO_VERBOSE_NAME = 'Видео'
ANIMAL_VIDEO_VERBOSE_NAME_PLURAL = ANIMAL_VIDEO_VERBOSE_NAME

# video_url
ANIMAL_VIDEO_VIDEO_URL = 'video_url'
ANIMAL_VIDEO_KEY_VIDEO_URL = 'Ссылка на видео Youtube'
ANIMAL_VIDEO_KEY_VIDEO_URL_HELP_TEXT = 'Для копирования ссылки воспользуйтесь кнопкой "Поделиться". '  \
                                            'Для вставки видео из VK ' \
                                            'необходимо получить текст с помощью кнопки "Еще=>Экспортировать" ' \
                                            'или с помощью правой кнопки мыши выбрать "Копировать код для встраивания", ' \
                                            'Ссылка для вставки включена в атрибуте src="ссылка_для_вставки".' \
                                            'Пример: ' \
                                            '"https://vk.com/video_ext.php?oid=-73666865&id=456239056&hash=cdc8d9d45257bb7d"'
ANIMAL_VIDEO_VIDEO_URL_VALIDATION_MESSAGE = 'Ссылка должна быть на видео.'

# description
ANIMAL_VIDEO_DESCRIPTION = 'description'
ANIMAL_VIDEO_KEY_DESCRIPTION = 'Название видео'
ANIMAL_VIDEO_KEY_DESCRIPTION_HELP_TEXT = 'Кратко опишите содержание видео. ' \
                                         'Описание будет использовано в качестве заголовка.'

# put_to_index_page
ANIMAL_VIDEO_PUT_TO_INDEX_PAGE = 'put_to_index_page'
ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE = 'Поместить на стартовую'
ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE_HELP_TEXT = 'Используется самое позднее видео.'

# show
ANIMAL_VIDEO_SHOW = SHOW
ANIMAL_VIDEO_KEY_SHOW = 'Показывать видео'
ANIMAL_VIDEO_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть.'

ANIMAL_VIDEO_FRAME_WIDTH = 480
ANIMAL_VIDEO_FRAME_HEIGHT = 390

ANIMAL_VIDEO_YOUTUBE_EMBED_URL = "http://www.youtube.com/embed/{video_id}"


ANIMAL_VIDEO_FRAME_TEMPLATE = '<iframe title="{dscr}" width="{width}" height="{height}" ' \
                                      'src="{url}" ' \
                                      'frameborder="0" allowfullscreen></iframe>'



# class Group
GROUP_VERBOSE_NAME = 'Группа'
GROUP_VERBOSE_NAME_PLURAL = 'Группы'

GROUP_ID = 'group_id'

# name
GROUP_NAME = 'name'
GROUP_KEY_NAME = 'Имя'
GROUP_KEY_NAME_HELP_TEXT = 'Данная группа появится на сайте как раздел меню в вкладке "Наши коты"'
GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT = 'Группа "{name}" имеет недопустимое значение.'

# description
GROUP_DESCRIPTION = 'description'
GROUP_KEY_DESCRIPTION = 'Описание'
GROUP_KEY_DESCRIPTION_HELP_TEXT = 'Краткое описание группы'

# show
GROUP_SHOW = SHOW
GROUP_KEY_SHOW = 'Показывать группу'
GROUP_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть. ' \
                           'Скрытые группы доступны для персонала на сайте.'

# instances Group

GROUP_INSTANCE_ALL_ID = 'all'
GROUP_INSTANCE_ALL_NAME = 'Все котики'
GROUP_INSTANCE_ALL_DESCR = 'Все животные которые попали к нам в приют.'

GROUP_INSTANCE_HOME_ID = ANIMAL_LOCATION_STATUS_HOME
GROUP_INSTANCE_HOME_NAME = 'Пристроены'
GROUP_INSTANCE_HOME_DESCR = 'Они обрели свой дом'

GROUP_INSTANCE_SHELTER_ID = ANIMAL_LOCATION_STATUS_SHELTER
GROUP_INSTANCE_SHELTER_NAME = 'Ищут дом'
GROUP_INSTANCE_SHELTER_DESCR = 'Собаки привязываются к людям, кошки привязываются к дому. ' \
                                       'Не дай этим котикам привязаться к клетке. Помоги им обрести свой дом.'
GROUP_INSTANCE_DEAD_ID = ANIMAL_LOCATION_STATUS_DEAD
GROUP_INSTANCE_DEAD_NAME = ANIMAL_LOCATION_STATUS_CHOICE_DEAD
GROUP_INSTANCE_DEAD_DESCR = 'Пусть земля им будет пухом, они всегда останутся в наших сердцах.'


GROUP_MAPPING = {
    GROUP_INSTANCE_ALL_ID: {
        NAME: GROUP_INSTANCE_ALL_NAME,
        DESCRIPTION: GROUP_INSTANCE_ALL_DESCR,
    },
    GROUP_INSTANCE_HOME_ID: {
        NAME: GROUP_INSTANCE_HOME_NAME,
        DESCRIPTION: GROUP_INSTANCE_HOME_DESCR,
    },
    GROUP_INSTANCE_SHELTER_ID: {
        NAME: GROUP_INSTANCE_SHELTER_NAME,
        DESCRIPTION: GROUP_INSTANCE_SHELTER_DESCR,
    },
    GROUP_INSTANCE_DEAD_ID: {
        NAME: GROUP_INSTANCE_DEAD_NAME,
        DESCRIPTION: GROUP_INSTANCE_DEAD_DESCR,
    },
}

PRIVATE_GROUP = (
    GROUP_INSTANCE_DEAD_ID,
)

GROUP_ANIMALS_PREVIEW_COUNT = 3


# class FilterForm

# age_distance
AGE_DISTANCE = 'age_distance'
AGE_DISTANCE_KEY = 'Возраст'
AGE_DISTANCE_CHOICES = (
    NO_CHOICE,
    ('_y1', 'до года'),
    ('y1_y3', 'от года до трех'),
    ('y3_', 'более трех лет'),
)

# shelter_distance
SHELTER_DISTANCE = 'shelter_distance'
SHELTER_DISTANCE_KEY = 'Время в приюте'
SHELTER_DISTANCE_CHOICES = (
    NO_CHOICE,
    ('_m1', 'до месяца'),
    ('m1_m6', 'от месяца до полугода'),
    ('m6_y1', 'от полугода до года'),
    ('y1_y2', 'от года до двух'),
    ('y2_', 'более двух лет'),
)

