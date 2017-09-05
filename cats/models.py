from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Group(models.Model):
    name = models.CharField('Имя', max_length=32, unique=True)
    description = models.TextField('Описание', blank=True, default=None)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class FieldType(models.Model):
    name = models.CharField('Название', max_length=32, unique=True)
    description = models.CharField('Описание', max_length=32, blank=True, default=None)

    class Meta:
        verbose_name = 'Тип особенности'
        verbose_name_plural = 'Типы особенностей'

    def __str__(self):
        return self.name


class FieldValue(models.Model):
    field_type = models.ForeignKey(FieldType)
    value_text = models.CharField('Значение (текст)', max_length=32, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Значение особенности'
        verbose_name_plural = 'Значения особенностей'

    def __str__(self):
        val = self.value_text
        return '{field_type}: {val}'.format(field_type=self.field_type, val=val)


class Animal(models.Model):
    name = models.CharField('Имя', max_length=32, unique=True, blank=True, default=None)
    # TODO: Create sex field
    created = models.DateTimeField('Дата публикации', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Дата обновления', auto_now_add=False, auto_now=True)
    date_of_birth = models.DateTimeField('Дата рождения', blank=True, null=True, default=None)
    group = models.ForeignKey(Group, verbose_name=Group._meta.verbose_name, blank=True, null=True, default=None)
    show = models.BooleanField('Показывать', default=True)
    field_value = models.ManyToManyField(
        FieldValue, verbose_name=FieldValue._meta.verbose_name, blank=True, default=None
    )

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    def get_hashtag_name(self):
        if self.name:
            template = '#{name}_catsekb'
            return template.format(name=self.__str__())

    def get_instagram_link(self):
        if self.name:
            template = 'https://www.instagram.com/explore/tags/{name}_catsekb/'
            return template.format(name=self.__str__())

    def get_description(self):

        """

        :rtype: AnimalDescription
        """
        return AnimalDescription.objects.get(animal=self)
    
    def get_image(self):
        """

        :rtype: AnimalImage
        """
        return AnimalImage.objects.get(animal=self)


class AnimalDescription(models.Model):
    animal = models.OneToOneField(Animal, unique=True, blank=True, default=None)
    description = models.TextField('Описание', blank=True, default=None)

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'

    def __str__(self):
        return 'Описание: {}'.format(self.animal)


class AnimalImage(models.Model):
    animal = models.OneToOneField(Animal)
    image = models.ImageField('Изображение', upload_to='images/')
    image_url = models.URLField('URL изображения', blank=True, default=None)
    alt = models.CharField('Подпись к фото', max_length=50)
    width = models.IntegerField('Ширина', blank=True, default=None, null=True)
    height = models.IntegerField('Высота', blank=True, default=None, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

