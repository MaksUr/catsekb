from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, BooleanField, ManyToManyField, \
    URLField, IntegerField, DateField, ImageField
# Create your models here.
from django.urls import reverse

from cats.constants import ANIMAL_IMAGE_VERBOSE_NAME_PLURAL, ANIMAL_IMAGE_VERBOSE_NAME, \
    ANIMAL_IMAGE_KEY_IMAGE_URL, HASHTAG_TEMPLATE_INSTAGRAM, \
    HASHTAG_TEMPLATE, HASHTAG_SUFFIX, \
    ANIMAL_VERBOSE_NAME_PLURAL, ANIMAL_VERBOSE_NAME, ANIMAL_KEY_UPDATED, ANIMAL_KEY_CREATED, ANIMAL_KEY_SHOW, \
    ANIMAL_KEY_DATE_OF_BIRTH, ANIMAL_KEY_BIRTHDAY_PRECISION, ANIMAL_KEY_SEX, ANIMAL_KEY_NAME, \
    ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_MONTH, ANIMAL_BIRTHDAY_PRECISION_YEAR, \
    FIELD_VALUE_STR_TEMPLATE, \
    FIELD_VALUE_VERBOSE_NAME_PLURAL, FIELD_VALUE_VERBOSE_NAME, FIELD_VALUE_KEY_VALUE_TEXT, \
    FIELD_TYPE_VERBOSE_NAME_PLURAL, FIELD_TYPE_VERBOSE_NAME, FIELD_TYPE_KEY_DESCRIPTION, FIELD_TYPE_KEY_NAME, \
    GROUP_VERBOSE_NAME_PLURAL, GROUP_VERBOSE_NAME, GROUP_KEY_SHOW, GROUP_KEY_DESCRIPTION, GROUP_KEY_NAME, \
    URL_NAME_ANIMAL, DJ_PK, ANIMAL_KEY_DESCRIPTION, \
    ANIMAL_KEY_LOCATION_STATUS, ANIMAL_SEX_CHOICES, ANIMAL_BIRTHDAY_PRECISION_CHOICES, ANIMAL_LOCATION_STATUS_CHOICES, \
    ANIMAL_KEY_TAG, URL_NAME_GROUP, ANIMAL_IMAGE_KEY_BACKGROUND, ANIMAL_IMAGE_KEY_FAVOURITE, \
    ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION, ANIMAL_LOCATION_STATUS_CHOICES_D, ANIMAL_SEX_CHOICES_D, \
    ANIMAL_KEY_VK_ALBUM_ID, ANIMAL_IMAGE_ANIMAL, ANIMAL_IMAGE_KEY_PHOTO_ID, ANIMAL_IMAGE_PHOTO_ID, \
    ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL, ANIMAL_IMAGE_KEY_IMAGE_THUMB, ANIMAL_IMAGE_KEY_CREATED
from cats.query import AnimalQuerySet
from cats.time import calc_age_uptoday
from cats.validators import group_name_validator, background_y_position_validator
from cats.vk_api.vk_import import get_vk_url_from_album_id


class Group(Model):
    name = CharField(GROUP_KEY_NAME, max_length=32, unique=True, validators=[group_name_validator])
    description = TextField(GROUP_KEY_DESCRIPTION, blank=True, default=None, max_length=100)
    show = BooleanField(GROUP_KEY_SHOW, default=True)

    class Meta:
        verbose_name = GROUP_VERBOSE_NAME
        verbose_name_plural = GROUP_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name

    @staticmethod
    def get_group_with_certain_settings(name, group_id, description=''):
        res = Group(name=name, id=group_id, show=True, description=description)
        return res

    def get_absolute_url(self):
        return reverse(URL_NAME_GROUP, kwargs={DJ_PK: self.id})

    def id_str(self):
        return str(self.id)


class FieldType(Model):
    name = CharField(FIELD_TYPE_KEY_NAME, max_length=32, unique=True)
    description = CharField(FIELD_TYPE_KEY_DESCRIPTION, max_length=32, blank=True, default=None)

    class Meta:
        verbose_name = FIELD_TYPE_VERBOSE_NAME
        verbose_name_plural = FIELD_TYPE_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name


class FieldValue(Model):
    field_type = ForeignKey(FieldType)
    value_text = CharField(FIELD_VALUE_KEY_VALUE_TEXT, max_length=32, blank=True, null=True, default=None)

    class Meta:
        verbose_name = FIELD_VALUE_VERBOSE_NAME
        verbose_name_plural = FIELD_VALUE_VERBOSE_NAME_PLURAL

    def __str__(self):
        val = self.value_text
        return FIELD_VALUE_STR_TEMPLATE.format(field_type=self.field_type, val=val)


class Animal(Model):
    BIRTHDAY_PRECISION_Y = ANIMAL_BIRTHDAY_PRECISION_YEAR
    BIRTHDAY_PRECISION_M = ANIMAL_BIRTHDAY_PRECISION_MONTH
    BIRTHDAY_PRECISION_D = ANIMAL_BIRTHDAY_PRECISION_DAY

    # fields
    name = CharField(ANIMAL_KEY_NAME, max_length=32, blank=True, default='')
    description = TextField(ANIMAL_KEY_DESCRIPTION, blank=True, default='')
    sex = CharField(ANIMAL_KEY_SEX, max_length=1, choices=ANIMAL_SEX_CHOICES, blank=True, default='')
    birthday_precision = CharField(
        ANIMAL_KEY_BIRTHDAY_PRECISION, max_length=1, choices=ANIMAL_BIRTHDAY_PRECISION_CHOICES, null=True, default=''
    )
    tag = CharField(ANIMAL_KEY_TAG, max_length=32, blank=True, default='')
    vk_album_id = IntegerField(ANIMAL_KEY_VK_ALBUM_ID, blank=True, default=None, null=True)
    date_of_birth = DateField(ANIMAL_KEY_DATE_OF_BIRTH, null=True, default=None, blank=True)
    # TODO: Применить данное поле, добавить метод отображение возроста по годам, месяцам и дням
    shelter_date = DateField("В приюте", null=True, default=None, blank=True)
    group = ForeignKey(Group, verbose_name=Group._meta.verbose_name, blank=True, null=True, default=None)
    show = BooleanField(ANIMAL_KEY_SHOW, default=True)
    field_value = ManyToManyField(
        FieldValue, verbose_name=FieldValue._meta.verbose_name, blank=True, default=None
    )
    location_status = CharField(
        ANIMAL_KEY_LOCATION_STATUS,
        max_length=1,
        choices=ANIMAL_LOCATION_STATUS_CHOICES,
        default='',
        blank=True
    )
    created = DateTimeField(ANIMAL_KEY_CREATED, null=True, default=None, blank=True)
    updated = DateTimeField(ANIMAL_KEY_UPDATED, auto_now_add=False, auto_now=True)

    objects = AnimalQuerySet.as_manager()

    class Meta:
        verbose_name = ANIMAL_VERBOSE_NAME
        verbose_name_plural = ANIMAL_VERBOSE_NAME_PLURAL

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    def get_name_for_tag(self):
        res = self.tag or self.__str__()
        return res.replace(' ', '_')

    def get_hashtag_name(self):
        name = self.get_name_for_tag()
        if name:
            template = HASHTAG_TEMPLATE
            return template.format(name=name, suffix=HASHTAG_SUFFIX)

    def get_instagram_link(self):
        name = self.get_name_for_tag()
        if name:
            template = HASHTAG_TEMPLATE_INSTAGRAM
            return template.format(name=name, suffix=HASHTAG_SUFFIX)

    def get_main_image(self):
        """

        :rtype: AnimalImage
        """
        res = self.get_image(favourite=True) or self.get_image()
        return res

    def get_background_image(self):
        """

        :rtype: AnimalImage
        """
        return self.get_image(background=True) or self.get_image()

    def get_image(self, **kwargs):
        """

        :rtype: AnimalImage
        """
        kwargs['animal'] = self
        res = AnimalImage.objects.filter(**kwargs).first()  # TODO: только избранные фото
        return res

    def get_age(self):
        if self.date_of_birth:
            return calc_age_uptoday(before_date=self.date_of_birth, later_date=date.today())
        else:
            return None

    def get_absolute_url(self):
        return reverse(URL_NAME_ANIMAL, kwargs={DJ_PK: self.id})

    def get_location_status(self):
        return ANIMAL_LOCATION_STATUS_CHOICES_D.get(self.location_status)

    def get_sex(self):
        return ANIMAL_SEX_CHOICES_D.get(self.sex)

    def get_vk_album_url(self):
        return get_vk_url_from_album_id(self.vk_album_id)

    def add_animal_image(self, **kwargs):
        kwargs[ANIMAL_IMAGE_ANIMAL] = self
        if kwargs.get(ANIMAL_IMAGE_PHOTO_ID) is not None:
            try:
                # TODO: получить только по полю id и animal
                AnimalImage.objects.get(**kwargs)
            except (AnimalImage.MultipleObjectsReturned,):
                return True
            except ObjectDoesNotExist:
                pass
            else:
                return True
        try:
            ai = AnimalImage(**kwargs)
        except TypeError:
            # TODO: check exceptions
            return False
        else:
            ai.save()
            return True


class AnimalImage(Model):
    animal = ForeignKey(Animal)
    image_url = URLField(ANIMAL_IMAGE_KEY_IMAGE_URL)
    image_small_url = URLField(ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL, blank=True, default=None, null=True)
    photo_id = IntegerField(ANIMAL_IMAGE_KEY_PHOTO_ID, blank=True, default=None, null=True)
    favourite = BooleanField(ANIMAL_IMAGE_KEY_FAVOURITE, default=False)
    background = BooleanField(ANIMAL_IMAGE_KEY_BACKGROUND, default=False)
    created = DateField(ANIMAL_IMAGE_KEY_CREATED, null=True, default=None, blank=True)
    background_y_position = IntegerField(
        ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION, blank=True, default=50, validators=[background_y_position_validator]
    )

    def image_thumb(self):
        # TODO: edit view
        image_url = self.image_small_url or self.image_url
        return '<img src="%s" style="height: 200px">' % image_url
    image_thumb.allow_tags = True
    image_thumb.short_description = ANIMAL_IMAGE_KEY_IMAGE_THUMB

    def image_url_tag(self):
        if self.image_url:
            res = '<a href="{url}">{label}</a>'.format(url=self.image_url, label=self.image_url)
        else:
            res = ''
        return res
    image_url_tag.allow_tags = True
    image_url_tag.short_description = ANIMAL_IMAGE_KEY_IMAGE_URL

    def image_small_url_tag(self):
        if self.image_small_url:
            res = '<a href="{url}">{label}</a>'.format(url=self.image_small_url, label=self.image_small_url)
        else:
            res = ''
        return res
    image_small_url_tag.allow_tags = True
    image_small_url_tag.short_description = ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL

    def get_background_style(self):
        res = 'background-image: url({url}); background-size: cover; background-position-y: {ypos}%;'.format(
            url=self.image_url, ypos=self.background_y_position
        )
        return res

    class Meta:
        verbose_name = ANIMAL_IMAGE_VERBOSE_NAME
        verbose_name_plural = ANIMAL_IMAGE_VERBOSE_NAME_PLURAL

    def __str__(self):
        return 'Фото "{id}": {animal}'.format(id=self.id, animal=self.animal)

    def get_alt(self):
        return self.__str__()


class Article(Model):  # TODO: create new application
    name = CharField("Название статьи", max_length=100)
    text = TextField("Текст статьи", blank=True, default='')

    def __str__(self):
        return self.name
