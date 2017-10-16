from datetime import date

from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, BooleanField, ManyToManyField, \
    OneToOneField, ImageField, URLField, IntegerField, DateField

# Create your models here.
from cats.constants import ANIMAL_IMAGE_VERBOSE_NAME_PLURAL, ANIMAL_IMAGE_VERBOSE_NAME, ANIMAL_IMAGE_KEY_HEIGHT, \
    ANIMAL_IMAGE_KEY_WIDTH, ANIMAL_IMAGE_KEY_ALT, ANIMAL_IMAGE_KEY_IMAGE_URL, ANIMAL_IMAGE_KEY_IMAGE, \
    HASHTAG_TEMPLATE_INSTAGRAM, HASHTAG_TEMPLATE, HASHTAG_SUFFIX, \
    ANIMAL_VERBOSE_NAME_PLURAL, ANIMAL_VERBOSE_NAME, ANIMAL_KEY_UPDATED, ANIMAL_KEY_CREATED, ANIMAL_KEY_SHOW, \
    ANIMAL_KEY_DATE_OF_BIRTH, ANIMAL_KEY_BIRTHDAY_PRECISION, ANIMAL_KEY_SEX, ANIMAL_KEY_NAME, \
    ANIMAL_BIRTHDAY_PRECISION_DAY_CHOICE, ANIMAL_BIRTHDAY_PRECISION_MONTH_CHOICE, ANIMAL_BIRTHDAY_PRECISION_YEAR_CHOICE, \
    ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_MONTH, ANIMAL_BIRTHDAY_PRECISION_YEAR, ANIMAL_SEX_FEMALE, \
    ANIMAL_SEX_MALE, ANIMAL_SEX_CHOICE_FEMALE, ANIMAL_SEX_CHOICE_MALE, FIELD_VALUE_STR_TEMPLATE, \
    FIELD_VALUE_VERBOSE_NAME_PLURAL, FIELD_VALUE_VERBOSE_NAME, FIELD_VALUE_KEY_VALUE_TEXT, \
    FIELD_TYPE_VERBOSE_NAME_PLURAL, FIELD_TYPE_VERBOSE_NAME, FIELD_TYPE_KEY_DESCRIPTION, FIELD_TYPE_KEY_NAME, \
    GROUP_VERBOSE_NAME_PLURAL, GROUP_VERBOSE_NAME, GROUP_KEY_SHOW, GROUP_KEY_DESCRIPTION, GROUP_KEY_NAME, \
    GROUP_ALL_ANIMALS_KEY_NAME, GROUP_ALL_ANIMALS_NAME, URL_NAME_ANIMAL, DJ_PK, ANIMAL_KEY_DESCRIPTION, \
    ANIMAL_KEY_LOCATION_STATUS, ANIMAL_SEX_CHOICES, ANIMAL_BIRTHDAY_PRECISION_CHOICES, ANIMAL_LOCATION_STATUS_CHOICES, \
    ANIMAL_LOCATION_STATUS_SHELTER
from cats.query import AnimalQuerySet
from cats.time import calc_age_uptoday


class Group(Model):
    name = CharField(GROUP_KEY_NAME, max_length=32, unique=True)
    description = TextField(GROUP_KEY_DESCRIPTION, blank=True, default=None)
    show = BooleanField(GROUP_KEY_SHOW, default=True)

    class Meta:
        verbose_name = GROUP_VERBOSE_NAME
        verbose_name_plural = GROUP_VERBOSE_NAME_PLURAL

    def __str__(self):
        return self.name

    @staticmethod
    def get_group_with_all_animals():
        res = Group(name=GROUP_ALL_ANIMALS_KEY_NAME, show=True, id=GROUP_ALL_ANIMALS_NAME)
        return res

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
    date_of_birth = DateField(ANIMAL_KEY_DATE_OF_BIRTH, null=True, default=None, blank=True)
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
    # TODO: add vk_album_url field
    created = DateTimeField(ANIMAL_KEY_CREATED, auto_now_add=True, auto_now=False)
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

    def get_hashtag_name(self):
        if self.name:
            template = HASHTAG_TEMPLATE
            return template.format(name=self.__str__(), suffix=HASHTAG_SUFFIX)

    def get_instagram_link(self):
        if self.name:
            template = HASHTAG_TEMPLATE_INSTAGRAM
            return template.format(name=self.__str__(), suffix=HASHTAG_SUFFIX)

    def get_image(self):
        """

        :rtype: AnimalImage
        """
        return AnimalImage.objects.get(animal=self)

    def get_age(self):
        if self.date_of_birth:
            return calc_age_uptoday(before_date=self.date_of_birth, later_date=date.today())
        else:
            return None

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(URL_NAME_ANIMAL, kwargs={DJ_PK: self.id})

    def get_location_status(self):
        # TODO: replace tuple to dict in constants
        if self.location_status == 'S':
            return 'В приюте'
        elif self.location_status == 'H':
            return 'Пристроен'
        else:
            return 'На радуге'


class AnimalImage(Model):
    animal = ForeignKey(Animal)
    image_url = URLField(ANIMAL_IMAGE_KEY_IMAGE_URL, default=None)
    alt = CharField(ANIMAL_IMAGE_KEY_ALT, max_length=50)
    width = IntegerField(ANIMAL_IMAGE_KEY_WIDTH, blank=True, default=None, null=True)
    height = IntegerField(ANIMAL_IMAGE_KEY_HEIGHT, blank=True, default=None, null=True)
    favourite = BooleanField("Избранное", default=False)

    def image_thumb(self):
        # TODO: edit view
        if self.image_url:
            return '<img src="%s" height="200" />' % self.image_url
        else:
            return '<img src="%s" height="200" />' % r'https://a.d-cd.net/8338b22s-960.jpg'
    image_thumb.allow_tags = True

    class Meta:
        verbose_name = ANIMAL_IMAGE_VERBOSE_NAME
        verbose_name_plural = ANIMAL_IMAGE_VERBOSE_NAME_PLURAL

