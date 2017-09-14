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
ANIMAL_IMAGE_KEY_HEIGHT_HELP_TEXT = '_Вспомогательный текст для ANIMAL_IMAGE_KEY_HEIGHT'

ANIMAL_IMAGE_KEY_WIDTH = 'Ширина'
ANIMAL_IMAGE_KEY_WIDTH_HELP_TEXT = '_Вспомогательный текст для ANIMAL_IMAGE_KEY_WIDTH'

ANIMAL_IMAGE_KEY_ALT = 'Подпись к фото'
ANIMAL_IMAGE_KEY_ALT_HELP_TEXT = '_Вспомогательный текст для ANIMAL_IMAGE_KEY_ALT'

ANIMAL_IMAGE_KEY_IMAGE_URL = 'URL изображения'
ANIMAL_IMAGE_KEY_IMAGE_URL_HELP_TEXT = '_Вспомогательный текст для ANIMAL_IMAGE_KEY_IMAGE_URL'

ANIMAL_IMAGE_KEY_IMAGE = 'Изображение'
ANIMAL_IMAGE_KEY_IMAGE_HELP_TEXT = '_Вспомогательный текст для ANIMAL_IMAGE_KEY_IMAGE'


ANIMAL_DESCRIPTION_STR_TEMPLATE = 'Описание: {animal}'
ANIMAL_DESCRIPTION_VERBOSE_NAME_PLURAL = 'Описания'
ANIMAL_DESCRIPTION_VERBOSE_NAME = 'Описание'

ANIMAL_DESCRIPTION_KEY_DESCRIPTION = 'Описание'
ANIMAL_DESCRIPTION_KEY_DESCRIPTION_HELP_TEXT = '_Вспомогательный текст для ANIMAL_DESCRIPTION_KEY_DESCRIPTION'


ANIMAL_VERBOSE_NAME_PLURAL = 'Питомцы'
ANIMAL_VERBOSE_NAME = 'Питомец'

ANIMAL_UPDATED = 'updated'
ANIMAL_KEY_UPDATED = 'Дата обновления'
ANIMAL_KEY_UPDATED_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_UPDATED'

ANIMAL_CREATED = 'created'
ANIMAL_KEY_CREATED = 'Дата публикации'
ANIMAL_KEY_CREATED_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_CREATED'

ANIMAL_SHOW = 'show'
ANIMAL_KEY_SHOW = 'Показывать котика'
ANIMAL_KEY_SHOW_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_SHOW'

ANIMAL_DATE_OF_BIRTH = 'date_of_birth'
ANIMAL_KEY_DATE_OF_BIRTH = 'День рождения'
ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_DATE_OF_BIRTH'

ANIMAL_NAME = 'name'
ANIMAL_KEY_NAME = 'Имя'
ANIMAL_KEY_NAME_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_NAME'
ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST = '"{name}" уже сущесвтует'

ANIMAL_BIRTHDAY_PRECISION = 'birthday_precision'
ANIMAL_KEY_BIRTHDAY_PRECISION = 'Точность даты рождения'
ANIMAL_KEY_BIRTHDAY_PRECISION_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_BIRTHDAY_PRECISION'
ANIMAL_BIRTHDAY_PRECISION_DAY_CHOICE = "до дня"
ANIMAL_BIRTHDAY_PRECISION_MONTH_CHOICE = "до месяца"
ANIMAL_BIRTHDAY_PRECISION_YEAR_CHOICE = "до года"

ANIMAL_BIRTHDAY_PRECISION_DAY = "D"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_MONTH = "M"  # для хранения в БД
ANIMAL_BIRTHDAY_PRECISION_YEAR = "Y"  # для хранения в БД

ANIMAL_SEX = 'sex'
ANIMAL_KEY_SEX = 'Пол'
ANIMAL_KEY_SEX_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_SEX'
ANIMAL_SEX_FEMALE = "F"  # для хранения в БД
ANIMAL_SEX_MALE = "M"  # для хранения в БД
ANIMAL_SEX_CHOICE_FEMALE = "Женский"
ANIMAL_SEX_CHOICE_MALE = "Мужской"

ANIMAL_DAYS = 'days'
ANIMAL_FORM_KEY_DAYS = 'Дней'
ANIMAL_KEY_DAYS_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_DAYS'

ANIMAL_MONTHS = 'months'
ANIMAL_FORM_KEY_MONTHS = 'Месяцев'
ANIMAL_KEY_MONTHS_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_MONTHS'

ANIMAL_YEARS = 'years'
ANIMAL_FORM_KEY_YEARS = 'Лет'
ANIMAL_KEY_YEARS_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_YEARS'

ANIMAL_FIELD_VALUE = 'field_value'
ANIMAL_KEY_FIELD_VALUE_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_FIELD_VALUE\n'

ANIMAL_GROUP = 'group'
ANIMAL_KEY_GROUP_HELP_TEXT = '_Вспомогательный текст для ANIMAL_KEY_GROUP'
ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS = 'Группа "{type}" имеет более одного значения.'

FIELD_VALUE_STR_TEMPLATE = '{field_type}: {val}'
FIELD_VALUE_VERBOSE_NAME_PLURAL = 'Значения особенностей'
FIELD_VALUE_VERBOSE_NAME = 'Значение особенности'
FIELD_VALUE_KEY_VALUE_TEXT = 'Значение (текст)'
FIELD_VALUE_KEY_VALUE_TEXT_HELP_TEXT = '_Вспомогательный текст для FIELD_VALUE_KEY_VALUE_TEXT'
FIELD_TYPE_VERBOSE_NAME_PLURAL = 'Типы особенностей'
FIELD_TYPE_VERBOSE_NAME = 'Тип особенности'
FIELD_TYPE_KEY_DESCRIPTION = 'Описание'
FIELD_TYPE_KEY_DESCRIPTION_HELP_TEXT = '_Вспомогательный текст для FIELD_TYPE_KEY_DESCRIPTION'
FIELD_TYPE_KEY_NAME = 'Название'
FIELD_TYPE_KEY_NAME_HELP_TEXT = '_Вспомогательный текст для FIELD_TYPE_KEY_NAME'

GROUP_VERBOSE_NAME_PLURAL = 'Группы'
GROUP_VERBOSE_NAME = 'Группа'
GROUP_KEY_SHOW = 'Показывать группу'
GROUP_KEY_SHOW_HELP_TEXT = '_Вспомогательный текст для GROUP_KEY_SHOW'
GROUP_KEY_DESCRIPTION = 'Описание'
GROUP_KEY_DESCRIPTION_HELP_TEXT = '_Вспомогательный текст для GROUP_KEY_DESCRIPTION'
GROUP_KEY_NAME = 'Имя'
GROUP_KEY_NAME_HELP_TEXT = '_Вспомогательный текст для GROUP_KEY_NAME'

HASHTAG_TEMPLATE_INSTAGRAM = 'https://www.instagram.com/explore/tags/{name}_{suffix}/'
HASHTAG_TEMPLATE = '#{name}_{suffix}'
HASHTAG_SUFFIX = 'catsekb'


DJ_INSTANCE = 'instance'
DJ_INITIAL = 'initial'



