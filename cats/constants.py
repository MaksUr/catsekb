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


# Служебные переменные
DJ_INSTANCE = 'instance'
DJ_INITIAL = 'initial'
DJ_CLASSES_COLLAPSE = 'collapse'
DJ_CLASSES = 'classes'
DJ_FIELDS = 'fields'
# URLs
URL_NAME_GROUP = 'group'
URL_NAME_GROUPS = 'groups'
URL_NAME_ANIMAL = 'animal'
URL_NAME_INDEX = 'index'


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
ANIMAL_IMAGE_KEY_IMAGE_URL = 'URL изображения'
ANIMAL_IMAGE_KEY_WIDTH_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_WIDTH'

# alt
ANIMAL_IMAGE_ALT = 'alt'
ANIMAL_IMAGE_KEY_ALT = 'Подпись к фото'
ANIMAL_IMAGE_KEY_HEIGHT_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_HEIGHT'

# width
ANIMAL_IMAGE_WIDTH = 'width'
ANIMAL_IMAGE_KEY_WIDTH = 'Ширина'
ANIMAL_IMAGE_KEY_IMAGE_URL_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_IMAGE_URL'

# height
ANIMAL_IMAGE_HEIGHT = 'height'
ANIMAL_IMAGE_KEY_HEIGHT = 'Высота'
ANIMAL_IMAGE_KEY_ALT_HELP_TEXT = '_help_text ANIMAL_IMAGE_KEY_ALT'


# class AnimalDescription
ANIMAL_DESCRIPTION_VERBOSE_NAME = 'Описание'
ANIMAL_DESCRIPTION_VERBOSE_NAME_PLURAL = 'Описания'
ANIMAL_DESCRIPTION_STR_TEMPLATE = 'Описание: {animal}'

# animal (foreign key for class Animal)
ANIMAL_DESCRIPTION_ANIMAL = 'description'
ANIMAL_DESCRIPTION_KEY_ANIMAL = 'Описание'
ANIMAL_DESCRIPTION_KEY_ANIMAL_HELP_TEXT = '_help_text ANIMAL_DESCRIPTION_KEY_DESCRIPTION'

# description
ANIMAL_DESCRIPTION_DESCRIPTION = 'description'
ANIMAL_DESCRIPTION_KEY_DESCRIPTION = 'Описание'
ANIMAL_DESCRIPTION_KEY_DESCRIPTION_HELP_TEXT = '_help_text ANIMAL_DESCRIPTION_KEY_DESCRIPTION'


# class Animal
ANIMAL_VERBOSE_NAME_PLURAL = 'Питомцы'
ANIMAL_VERBOSE_NAME = 'Питомец'
ANIMAL_MAIN_FIELD_SET = 'Общая информация'

HASHTAG_TEMPLATE_INSTAGRAM = 'https://www.instagram.com/explore/tags/{name}_{suffix}/'
HASHTAG_TEMPLATE = '#{name}_{suffix}'
HASHTAG_SUFFIX = 'catsekb'

# name
ANIMAL_NAME = 'name'
ANIMAL_KEY_NAME = 'Имя'
ANIMAL_KEY_NAME_HELP_TEXT = '_help_text ANIMAL_KEY_NAME'
ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST = '"{name}" уже сущесвтует'
ANIMAL_NAME_DEFAULT = 'Котик'  # Имя котика по дефолту, если имя не указано.

# sex
ANIMAL_SEX = 'sex'
ANIMAL_KEY_SEX = 'Пол'
ANIMAL_KEY_SEX_HELP_TEXT = '_help_text ANIMAL_KEY_SEX'

ANIMAL_SEX_FEMALE = "F"  # для хранения в БД
ANIMAL_SEX_MALE = "M"  # для хранения в БД
ANIMAL_SEX_CHOICE_FEMALE = "Женский"
ANIMAL_SEX_CHOICE_MALE = "Мужской"

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

# date_of_birth
# При выборе этого поля, при сохранении возраст (days, months, years) устанавливается автоматом.
ANIMAL_DATE_OF_BIRTH = 'date_of_birth'
ANIMAL_KEY_DATE_OF_BIRTH = 'День рождения'
ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT = '_help_text ANIMAL_KEY_DATE_OF_BIRTH'

# group
ANIMAL_GROUP = 'group'
ANIMAL_KEY_GROUP_HELP_TEXT = '_help_text ANIMAL_KEY_GROUP'
ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS = 'Группа "{type}" имеет более одного значения.'

# show
ANIMAL_SHOW = 'show'
ANIMAL_KEY_SHOW = 'Показывать котика'
ANIMAL_KEY_SHOW_HELP_TEXT = '_help_text ANIMAL_KEY_SHOW'

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
FIELD_VALUE_VERBOSE_NAME = 'Значение особенности'
FIELD_VALUE_VERBOSE_NAME_PLURAL = 'Значения особенностей'
FIELD_VALUE_STR_TEMPLATE = '{field_type}: {val}'

# value_text
FIELD_VALUE_VALUE_TEXT = 'value_text'
FIELD_VALUE_KEY_VALUE_TEXT = 'Значение (текст)'
FIELD_VALUE_KEY_VALUE_TEXT_HELP_TEXT = '_help_text FIELD_VALUE_KEY_VALUE_TEXT'

# field_type (foreign key for class FieldType)
FIELD_VALUE_FIELD_TYPE = 'field_type'
FIELD_VALUE_KEY_FIELD_TYPE = '_?'  # TODO: edit value
FIELD_VALUE_KEY_FIELD_TYPE_HELP_TEXT = '_help_text FIELD_VALUE_KEY_VALUE_TEXT'


# class FieldType
FIELD_TYPE_VERBOSE_NAME = 'Тип особенности'
FIELD_TYPE_VERBOSE_NAME_PLURAL = 'Типы особенностей'

# name
FIELD_TYPE_NAME = 'name'
FIELD_TYPE_KEY_NAME = 'Название'
FIELD_TYPE_KEY_NAME_HELP_TEXT = '_help_text FIELD_TYPE_KEY_NAME'

# description
FIELD_TYPE_DESCRIPTION = 'description'
FIELD_TYPE_KEY_DESCRIPTION = 'Описание'
FIELD_TYPE_KEY_DESCRIPTION_HELP_TEXT = '_help_text FIELD_TYPE_KEY_DESCRIPTION'


# class Group
GROUP_VERBOSE_NAME = 'Группа'
GROUP_VERBOSE_NAME_PLURAL = 'Группы'

GROUP_ALL_ANIMALS_KEY_NAME = 'Все питомцы'
GROUP_ALL_ANIMALS_NAME = 'all'

# name
GROUP_NAME = 'name'
GROUP_KEY_NAME = 'Имя'
GROUP_KEY_NAME_HELP_TEXT = '_help_text GROUP_KEY_NAME'

# description
GROUP_DESCRIPTION = 'description'
GROUP_KEY_DESCRIPTION = 'Описание'
GROUP_KEY_DESCRIPTION_HELP_TEXT = '_help_text GROUP_KEY_DESCRIPTION'

# show
GROUP_SHOW = 'show'
GROUP_KEY_SHOW = 'Показывать группу'
GROUP_KEY_SHOW_HELP_TEXT = '_help_text GROUP_KEY_SHOW'

ANIMAL_ANIMAL_LINK = 'animal_link'
ANIMAL_KEY_ANIMAL_LINK = 'Ссылка на сайт'
ANIMAL_KEY_ANIMAL_LINK_HELP_TEXT = '_help_text ANIMAL_KEY_ANIMAL_LINK'

