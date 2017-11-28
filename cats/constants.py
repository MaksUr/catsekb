# KEY - это название поля у которого есть значение.
# TEMPLATE - это шаблон. Переменные вставляются внуть скобок: '{название_поля} - {значение_поля}'
#
# verbose_name - название модели, plural - множ. число.
# field_set - объединение полей (заголовок)
#
# ANIMAL - питомец
# FIELD_TYPE - название свойства
# FIELD_VALUE - значение свойства
# GROUP - группа
#
# foreign_key служит для связи текущей модели с другой моделью. Например модель - AnimalImage,
# foreign_key: animal ссылается на модель Animal.
# Это значит поле animal в AnimalImage относится к определенному Animal

SHOW = 'show'

# Служебные переменные
DJ_INSTANCE = 'instance'
DJ_INITIAL = 'initial'
DJ_CLASSES_COLLAPSE = 'collapse'
DJ_CLASSES = 'classes'
DJ_FIELDS = 'fields'
DJ_PK = 'pk'
DJ_ID = 'id'
DJ_PAGE = 'page'
DJ_OBJECT = 'object'

# URLs
URL_NAME_INDEX = 'index'
URL_NAME_GROUPS = 'group_list'
URL_NAME_GROUP = 'group_detail'
URL_NAME_ANIMAL_FILTER = 'animal_filter'
URL_NAME_ANIMALS = 'animal_list'
URL_NAME_ANIMAL = 'animal_detail'

APPLICATION_VERBOSE_NAME = 'Котики'  # Название приложения

VK_GROUP_ID = 73666865

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
ANIMAL_IMAGE_BACKGROUND = 'background'
ANIMAL_IMAGE_KEY_BACKGROUND = 'Использовать для фона страницы с котом.'
ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT = 'Фоновое изображение страницы с котом. Рекомендуется использовать предпросмотр.'

# created
ANIMAL_IMAGE_CREATED = 'created'
ANIMAL_IMAGE_KEY_CREATED = 'Дата создания'
ANIMAL_IMAGE_KEY_CREATED_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_CREATED'

# background_y_position
ANIMAL_IMAGE_BACKGROUND_Y_POSITION = 'background_y_position'
ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION = 'Настройка позиции фонового изображения по вертикали.'
ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT = 'Значение от 0 до 100. Используется для корректного отображения вертикальных изображений'
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

# tag
ANIMAL_TAG_FIELD_SET = 'Настройка хэштега'

ANIMAL_TAG = 'tag'
ANIMAL_KEY_TAG = 'Редактирование хештега'
ANIMAL_KEY_TAG_HELP_TEXT = 'При заполнении этого поля, будет использоваться данный пользовательский хэштег.'

# tag display

ANIMAL_TAG_DISPLAY = 'tag_display'
ANIMAL_KEY_TAG_DISPLAY = 'Сгенерированный хэштег'
ANIMAL_KEY_TAG_DISPLAY_HELP_TEXT = 'Убедитесь в корректности ссылки.'  # TODO: display in admin form

HASHTAG_TEMPLATE_INSTAGRAM = 'https://www.instagram.com/explore/tags/{name}_{suffix}/'
HASHTAG_TEMPLATE = '#{name}_{suffix}'
HASHTAG_SUFFIX = 'catsekb'

# name
ANIMAL_NAME = 'name'
ANIMAL_KEY_NAME = 'Имя'
ANIMAL_KEY_NAME_HELP_TEXT = '_help_text ANIMAL_KEY_NAME'
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
ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT = 'Перед обновлением сохранить ссылку на альбом.'

# sex
ANIMAL_SEX = 'sex'
ANIMAL_KEY_SEX = 'Пол'
ANIMAL_KEY_SEX_HELP_TEXT = '_help_text ANIMAL_KEY_SEX'

ANIMAL_SEX_FEMALE = "F"  # для хранения в БД
ANIMAL_SEX_MALE = "M"  # для хранения в БД
ANIMAL_SEX_CHOICE_FEMALE = "Женский"
ANIMAL_SEX_CHOICE_MALE = "Мужской"
ANIMAL_SEX_CHOICES = (
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
ANIMAL_LOCATION_STATUS_CHOICE_SHELTER = 'Ищут дом'
ANIMAL_LOCATION_STATUS_CHOICE_DEAD = 'На радуге'
ANIMAL_LOCATION_STATUS_HOME_DESСR = 'Они обрели свой дом'
ANIMAL_LOCATION_STATUS_SHELTER_DESСR = 'Собаки привязываются к людям, кошки привязываются к дому. Не дай этим котикам привязаться к клетке. Помоги им обрести свой дом.'
ANIMAL_LOCATION_STATUS_DEAD_DESСR = 'Пусть земля им будет пухом, они всегда останутся в наших сердцах.'
ANIMAL_LOCATION_STATUS_CHOICES = (
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
ANIMAL_KEY_BIRTHDAY_PRECISION = 'Точность даты рождения'
ANIMAL_KEY_BIRTHDAY_PRECISION_HELP_TEXT = '_help_text ANIMAL_KEY_BIRTHDAY_PRECISION'

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
# При выборе этого поля, при сохранении возраст (days, months, years) устанавливается автоматом.
ANIMAL_DATE_OF_BIRTH = 'date_of_birth'
ANIMAL_KEY_DATE_OF_BIRTH = 'День рождения'
ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT = '_help_text ANIMAL_KEY_DATE_OF_BIRTH'

# shelter_date
ANIMAL_SHELTER_DATE = 'shelter_date'
ANIMAL_KEY_SHELTER_DATE = 'В приюте'
ANIMAL_KEY_SHELTER_DATE_HELP_TEXT = 'Примерная дата попадания в приют'

# group
ANIMAL_GROUP = 'group'
ANIMAL_KEY_GROUP_HELP_TEXT = '_help_text ANIMAL_KEY_GROUP'
ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS = 'Группа "{type}" имеет более одного значения.'

# show
ANIMAL_SHOW = SHOW
ANIMAL_KEY_SHOW = 'Показывать котика'
ANIMAL_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть.'

# valid_info
ANIMAL_VALID_INFO = 'valid_info'
ANIMAL_KEY_VALID_INFO = 'Проверено'
ANIMAL_KEY_VALID_INFO_HELP_TEXT = 'Информация проверена вручную.'

# field_value (foreign key)
ANIMAL_FIELD_VALUE = 'field_value'
ANIMAL_KEY_FIELD_VALUE_HELP_TEXT = '_help_text ANIMAL_KEY_FIELD_VALUE'

# created
ANIMAL_CREATED = 'created'
ANIMAL_KEY_CREATED = 'Дата публикации'
ANIMAL_KEY_CREATED_HELP_TEXT = '_help_text ANIMAL_KEY_CREATED'

# updated
ANIMAL_UPDATED = 'updated'
ANIMAL_KEY_UPDATED = 'Дата обновления'
ANIMAL_KEY_UPDATED_HELP_TEXT = '_help_text ANIMAL_KEY_UPDATED'

# Возраст. Определяет date_of_birth в том случае, если date_of_birth не редактировался пользователем.
ANIMAL_AGE_FIELD_SET = 'Настройки возраста'
# days (AnimalForm) - возраст
ANIMAL_DAYS = 'days'
ANIMAL_FORM_KEY_DAYS = 'Дней'
ANIMAL_KEY_DAYS_HELP_TEXT = '_help_text ANIMAL_KEY_DAYS'

# months (AnimalForm) - возраст
ANIMAL_MONTHS = 'months'
ANIMAL_FORM_KEY_MONTHS = 'Месяцев'
ANIMAL_KEY_MONTHS_HELP_TEXT = '_help_text ANIMAL_KEY_MONTHS'

# years (AnimalForm) - возраст
ANIMAL_YEARS = 'years'
ANIMAL_FORM_KEY_YEARS = 'Лет'
ANIMAL_KEY_YEARS_HELP_TEXT = '_help_text ANIMAL_KEY_YEARS'


# class FieldValue
# Только одно значение FieldValue в одном Animal может принадлежать одному FieldType
FIELD_VALUE_VERBOSE_NAME = 'Особенность'
FIELD_VALUE_VERBOSE_NAME_PLURAL = 'Значения особенностей'
FIELD_VALUE_STR_TEMPLATE = '{field_type} - {val}'

# value_text
FIELD_VALUE_VALUE_TEXT = 'value_text'
FIELD_VALUE_KEY_VALUE_TEXT = 'Особенность'
FIELD_VALUE_KEY_VALUE_TEXT_HELP_TEXT = '_help_text FIELD_VALUE_KEY_VALUE_TEXT'

# field_type (foreign key for class FieldType)
FIELD_VALUE_FIELD_TYPE = 'field_type'
FIELD_VALUE_KEY_FIELD_TYPE = '_?'  # TODO: edit value
FIELD_VALUE_KEY_FIELD_TYPE_HELP_TEXT = '_help_text FIELD_VALUE_KEY_VALUE_TEXT'


# class FieldType
FIELD_TYPE_VERBOSE_NAME = 'Тип особенности'
FIELD_TYPE_VERBOSE_NAME_PLURAL = 'Типы особенностей'
FIELD_TYPE_PREFIX = 'ft_'

# name
FIELD_TYPE_NAME = 'name'
FIELD_TYPE_KEY_NAME = 'Название'
FIELD_TYPE_KEY_NAME_HELP_TEXT = '_help_text FIELD_TYPE_KEY_NAME'

# description
FIELD_TYPE_DESCRIPTION = 'description'
FIELD_TYPE_KEY_DESCRIPTION = 'Описание'
FIELD_TYPE_KEY_DESCRIPTION_HELP_TEXT = '_help_text FIELD_TYPE_KEY_DESCRIPTION'

# FieldValue and FieldType instances
FIELD_TYPE_INST_LITTER_BOX_SKILL = 'Лоток'
FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_A = 'Без промаху'
FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_B = 'Научится'
FIELD_VALUE_INST_LITTER_BOX_SKILL_LEVEL_C = 'Имеются проблемы'

FIELD_TYPE_INST_RELATIONSHIPS_WITH_PEOPLE = 'Отношение к людям'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_A = 'Доброжелательное'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_B = 'Трусливое'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_PEOPLE_C = 'С характером'

FIELD_TYPE_INST_RELATIONSHIPS_WITH_ANIMALS = 'Отношение к другим животным'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_A = 'Доброжелательное'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_B = 'Стрессовое'
FIELD_VALUE_INST_RELATIONSHIPS_WITH_ANIMALS_C = 'Доминирующее'


# class Group
GROUP_VERBOSE_NAME = 'Группа'
GROUP_VERBOSE_NAME_PLURAL = 'Группы'

GROUP_ALL_ANIMALS_KEY_NAME = 'Все котики'
GROUP_ALL_ANIMALS_NAME = 'all'
GROUP_ALL_ANIMALS_NAME_DESCR = 'Все животные которые попали к нам в приют.'
GROUP_ID = 'group_id'

# name
GROUP_NAME = 'name'
GROUP_KEY_NAME = 'Имя'
GROUP_KEY_NAME_HELP_TEXT = '_help_text GROUP_KEY_NAME'
GROUP_FORM_VALIDATION_ERROR_NAME_IS_DEFAULT = 'Группа "{name}" имеет недопустимое значение.'

# description
GROUP_DESCRIPTION = 'description'
GROUP_KEY_DESCRIPTION = 'Описание'
GROUP_KEY_DESCRIPTION_HELP_TEXT = '_help_text GROUP_KEY_DESCRIPTION'

# show
GROUP_SHOW = SHOW
GROUP_KEY_SHOW = 'Показывать группу'
GROUP_KEY_SHOW_HELP_TEXT = 'Убрать отметку вместо удаления или чтобы скрыть.'

ANIMAL_ANIMAL_LINK = 'animal_link'
ANIMAL_KEY_ANIMAL_LINK = 'Ссылка на сайт'
ANIMAL_KEY_ANIMAL_LINK_HELP_TEXT = '_help_text ANIMAL_KEY_ANIMAL_LINK'


# class FilterForm

# age_distance
AGE_DISTANCE = 'age_distance'
AGE_DISTANCE_KEY = 'Возраст'
AGE_DISTANCE_CHOICES = (
    ('_d5', 'до 5 дней'),
    ('d5_m1', 'от 5 дней до месяца'),
    ('m1_m6', 'от месяца до полугода'),
    ('m6_y1', 'от полугода до года'),
    ('y1_y2', 'от года до двух'),
    ('y2_y5', 'от двух до пяти лет'),
    ('y5_', 'более пяти лет'),
)


# Captions
CAPTION_ANIMAL_LIST_DEFAULT = 'Наши коты'

# Menu
INDEX = 'index'
ANIMALS = 'animals'
HELPFUL = 'helpful'
CONTACTS = 'contacts'
