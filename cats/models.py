from datetime import date

import re
from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, BooleanField, ManyToManyField, \
    URLField, IntegerField, DateField, CASCADE
# Create your models here.
from django.urls import reverse

from cats.cats_constants import ANIMAL_IMAGE_VERBOSE_NAME_PLURAL, ANIMAL_IMAGE_VERBOSE_NAME, \
    ANIMAL_IMAGE_KEY_IMAGE_URL, HASHTAG_TEMPLATE_INSTAGRAM, \
    HASHTAG_TEMPLATE, HASHTAG_SUFFIX, \
    ANIMAL_VERBOSE_NAME_PLURAL, ANIMAL_VERBOSE_NAME, ANIMAL_KEY_UPDATED, ANIMAL_KEY_CREATED, ANIMAL_KEY_SHOW, \
    ANIMAL_KEY_SEX, ANIMAL_KEY_NAME, \
    ANIMAL_BIRTHDAY_PRECISION_DAY, ANIMAL_BIRTHDAY_PRECISION_MONTH, ANIMAL_BIRTHDAY_PRECISION_YEAR, \
    GROUP_VERBOSE_NAME_PLURAL, GROUP_VERBOSE_NAME, GROUP_KEY_SHOW, GROUP_KEY_DESCRIPTION, GROUP_KEY_NAME, \
    ANIMAL_KEY_DESCRIPTION, \
    ANIMAL_KEY_LOCATION_STATUS, ANIMAL_SEX_CHOICES, ANIMAL_BIRTHDAY_PRECISION_CHOICES, ANIMAL_LOCATION_STATUS_CHOICES, \
    ANIMAL_KEY_TAG, ANIMAL_IMAGE_KEY_BACKGROUND, ANIMAL_IMAGE_KEY_FAVOURITE, \
    ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION, ANIMAL_LOCATION_STATUS_CHOICES_D, ANIMAL_SEX_CHOICES_D, \
    ANIMAL_KEY_VK_ALBUM_ID, ANIMAL_IMAGE_KEY_PHOTO_ID, ANIMAL_IMAGE_KEY_IMAGE_SMALL_URL, ANIMAL_IMAGE_KEY_IMAGE_THUMB, \
    ANIMAL_IMAGE_KEY_CREATED, ANIMAL_KEY_SHELTER_DATE, ANIMAL_DAYS, ANIMAL_MONTHS, \
    ANIMAL_YEARS, GROUP_ANIMALS_PREVIEW_COUNT, ANIMAL_VIDEO_VERBOSE_NAME, ANIMAL_VIDEO_VERBOSE_NAME_PLURAL, \
    ANIMAL_VIDEO_KEY_VIDEO_URL, ANIMAL_VIDEO_KEY_DESCRIPTION, ANIMAL_VIDEO_FRAME_TEMPLATE, \
    ANIMAL_VIDEO_YOUTUBE_EMBED_URL, ANIMAL_VIDEO_KEY_SHOW, ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE, \
    ANIMAL_VIDEO_FRAME_WIDTH, ANIMAL_VIDEO_FRAME_HEIGHT

from catsekb.constants import DJ_PK, URL_NAME_GROUP, URL_NAME_ANIMAL, VK_GROUP_ID, CREATED, CREATED_KEY
from cats.query import AnimalQuerySet
from cats.time import calc_age_uptoday
from cats.validators import group_name_validator, background_y_position_validator

PROJECT_CHOICES = (
    ('catsekb', 'CatsEkb'),
    ('huskyekb', 'HuskyEkb'),
    ('rotvodom', 'Rotvodom'),
)


class Group(Model):
    # TODO: Выпилить группу
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

    def get_preview_animals_by_group(self):
        return Animal.objects.filter(group=self, show=True).order_by('?')[:GROUP_ANIMALS_PREVIEW_COUNT]


class AnimalVideo(Model):

    class Meta:
        verbose_name = ANIMAL_VIDEO_VERBOSE_NAME
        verbose_name_plural = ANIMAL_VIDEO_VERBOSE_NAME_PLURAL

    video_url = URLField(ANIMAL_VIDEO_KEY_VIDEO_URL)
    description = CharField(ANIMAL_VIDEO_KEY_DESCRIPTION, max_length=50)
    show = BooleanField(ANIMAL_VIDEO_KEY_SHOW, default=True)
    created = DateTimeField(CREATED_KEY, auto_now_add=True)
    put_to_index_page = BooleanField(ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE, default=False)
    important = True

    def __str__(self):
        return self.description

    PATTERN_YOUTUBE_ID = re.compile(
        r'(?:youtube(?:-nocookie)?\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/ ]{11})'
    )
    PATTERN_VK_VIDEO_URL = re.compile(r'^(https?:)?//vk\.com/video_ext\.php\?oid=-?\d+&id=\d+&hash=[\d\w]+(&hd=\d+)?$')

    @staticmethod
    def get_video_url(video_url):
        m = re.search(AnimalVideo.PATTERN_YOUTUBE_ID, video_url)
        if m:
            return ANIMAL_VIDEO_YOUTUBE_EMBED_URL.format(video_id=m.group(1))
        m = re.search(AnimalVideo.PATTERN_VK_VIDEO_URL, video_url)
        if m:
            return m.group()

    def get_frame(self):
        video_url = self.get_video_url(self.video_url)
        if video_url:
            return ANIMAL_VIDEO_FRAME_TEMPLATE.format(dscr=self.description, url=video_url,
                                                      width=ANIMAL_VIDEO_FRAME_WIDTH, height=ANIMAL_VIDEO_FRAME_HEIGHT)


class Animal(Model):
    BIRTHDAY_PRECISION_Y = ANIMAL_BIRTHDAY_PRECISION_YEAR
    BIRTHDAY_PRECISION_M = ANIMAL_BIRTHDAY_PRECISION_MONTH
    BIRTHDAY_PRECISION_D = ANIMAL_BIRTHDAY_PRECISION_DAY

    # fields
    name = CharField(ANIMAL_KEY_NAME, max_length=32, blank=True, default='')
    description = TextField(ANIMAL_KEY_DESCRIPTION, blank=True, default='')  # TODO: ReachTextField
    sex = CharField(ANIMAL_KEY_SEX, max_length=1, choices=ANIMAL_SEX_CHOICES[1:], blank=True, default='')
    project = CharField('Проект', max_length=10, choices=PROJECT_CHOICES)
    birthday_precision = CharField(
        max_length=1, choices=ANIMAL_BIRTHDAY_PRECISION_CHOICES, null=True, default=''
    )
    tag = CharField(ANIMAL_KEY_TAG, max_length=32, blank=True, default='')
    vk_album_id = IntegerField(ANIMAL_KEY_VK_ALBUM_ID, blank=True, default=None, null=True)
    date_of_birth = DateField(null=True, default=None, blank=True)
    shelter_date = DateField(ANIMAL_KEY_SHELTER_DATE, null=True, default=None, blank=True)
    group = ForeignKey(Group, on_delete=CASCADE, verbose_name=Group._meta.verbose_name, blank=True, null=True, default=None)
    video = ForeignKey(AnimalVideo, on_delete=CASCADE, verbose_name=AnimalVideo._meta.verbose_name, blank=True, null=True, default=None)
    show = BooleanField(ANIMAL_KEY_SHOW, default=True)
    location_status = CharField(
        ANIMAL_KEY_LOCATION_STATUS,
        max_length=1,
        choices=ANIMAL_LOCATION_STATUS_CHOICES[1:],
        default='',
        blank=True
    )
    created = DateTimeField(ANIMAL_KEY_CREATED, auto_now_add=True)
    updated = DateTimeField(ANIMAL_KEY_UPDATED, auto_now=True)

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
        # TODO: учесть birthday_precision
        if self.date_of_birth:
            d = calc_age_uptoday(before_date=self.date_of_birth, later_date=date.today())
            d = self.get_age_by_precision(d, self.birthday_precision)
            return d
        else:
            return None

    @staticmethod
    def get_age_by_precision(d, precision):
        # TODO: use from model
        if not precision or precision == Animal.BIRTHDAY_PRECISION_D:
            return d
        d[ANIMAL_DAYS] = None
        if precision == Animal.BIRTHDAY_PRECISION_M:
            return d
        d[ANIMAL_MONTHS] = None
        if precision == Animal.BIRTHDAY_PRECISION_Y:
            return d
        d[ANIMAL_YEARS] = None
        return d

    def get_absolute_url(self):
        return reverse(URL_NAME_ANIMAL, kwargs={DJ_PK: self.id})

    def get_location_status(self):
        return ANIMAL_LOCATION_STATUS_CHOICES_D.get(self.location_status)

    def get_sex(self):
        return ANIMAL_SEX_CHOICES_D.get(self.sex)

    def get_vk_album_url(self):
        if self.vk_album_id:
            return r"https://vk.com/album-{group_id}_{album_id}".format(group_id=VK_GROUP_ID, album_id=self.vk_album_id)
        else:
            return None

    def get_shelter_time(self):
        if self.shelter_date:
            return calc_age_uptoday(before_date=self.shelter_date, later_date=date.today())
        else:
            return None


class AnimalImage(Model):
    animal = ForeignKey(Animal, on_delete=CASCADE)
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
