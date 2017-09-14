# KEY - это название поля у которого есть значение.
# TEMPLATE - это шаблон. Переменные вставляются внуть скобок: '{название_поля} - {значение_поля}'
#
# verbose_name - название модели, plural - множ. число.
#
# ANIMAL - питомец
# FIELD_TYPE - название свойства
# FIELD_VALUE - значение свойства
# GROUP - группа

ANIMAL_IMAGE_VERBOSE_NAME_PLURAL = 'Фотографии'
ANIMAL_IMAGE_VERBOSE_NAME = 'Фотография'
ANIMAL_IMAGE_KEY_HEIGHT = 'Высота'
ANIMAL_IMAGE_KEY_WIDTH = 'Ширина'
ANIMAL_IMAGE_KEY_ALT = 'Подпись к фото'
ANIMAL_IMAGE_KEY_IMAGE_URL = 'URL изображения'
ANIMAL_IMAGE_KEY_IMAGE = 'Изображение'
ANIMAL_DESCRIPTION_STR_TEMPLATE = 'Описание: {animal}'
ANIMAL_DESCRIPTION_VERBOSE_NAME_PLURAL = 'Описания'
ANIMAL_DESCRIPTION_VERBOSE_NAME = 'Описание'
ANIMAL_DESCRIPTION_KEY_DESCRIPTION = 'Описание'
ANIMAL_VERBOSE_NAME_PLURAL = 'Питомцы'
ANIMAL_VERBOSE_NAME = 'Питомец'
ANIMAL_KEY_UPDATED = 'Дата обновления'
ANIMAL_KEY_CREATED = 'Дата публикации'
ANIMAL_KEY_SHOW = 'Показывать котика'
ANIMAL_KEY_DATE_OF_BIRTH = 'День рождения'
ANIMAL_KEY_BIRTHDAY_PRECISION = 'Точность даты рождения'
ANIMAL_KEY_SEX = 'Пол'
ANIMAL_KEY_NAME = 'Имя'
ANIMAL_BIRTHDAY_PRECISION_DAY_CHOICE = "до дня"
ANIMAL_BIRTHDAY_PRECISION_MONTH_CHOICE = "до месяца"
ANIMAL_BIRTHDAY_PRECISION_YEAR_CHOICE = "до года"
ANIMAL_BIRTHDAY_PRECISION_DAY = "D"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_MONTH = "M"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_YEAR = "Y"  # для хранения в БД
ANIMAL_SEX_FEMALE = "F"  # для хранения в БД
ANIMAL_SEX_MALE = "M"  # для хранения в БД
ANIMAL_SEX_CHOICE_FEMALE = "Женский"
ANIMAL_SEX_CHOICE_MALE = "Мужской"

FIELD_VALUE_STR_TEMPLATE = '{field_type}: {val}'
FIELD_VALUE_VERBOSE_NAME_PLURAL = 'Значения особенностей'
FIELD_VALUE_VERBOSE_NAME = 'Значение особенности'
FIELD_VALUE_KEY_VALUE_TEXT = 'Значение (текст)'
FIELD_TYPE_KEY_VERBOSE_NAME_PLURAL = 'Типы особенностей'
FIELD_TYPE_KEY_VERBOSE_NAME = 'Тип особенности'
FIELD_TYPE_KEY_DESCRIPTION = 'Описание'
FIELD_TYPE_KEY_NAME = 'Название'
GROUP_VERBOSE_NAME_PLURAL = 'Группы'
GROUP_VERBOSE_NAME = 'Группа'
GROUP_KEY_SHOW = 'Показывать группу'
GROUP_KEY_DESCRIPTION = 'Описание'
GROUP_KEY_NAME = 'Имя'

HASHTAG_TEMPLATE_INSTAGRAM = 'https://www.instagram.com/explore/tags/{name}_{suffix}/'
HASHTAG_TEMPLATE = '#{name}_{suffix}'
HASHTAG_SUFFIX = 'catsekb'
