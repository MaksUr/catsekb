from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField('Имя', max_length=32, unique=True)
    description = models.TextField('Описание', blank=True, default=None)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Animal(models.Model):
    name = models.CharField('Имя', max_length=32, unique=True)
    created = models.DateTimeField('Дата публикации', auto_now_add=True, auto_now=False)
    updated = models.DateTimeField('Дата обновления', auto_now_add=False, auto_now=True)
    date_of_birth = models.DateTimeField('Дата рождения', blank=True, null=True, default=None)
    group = models.ForeignKey(Group, blank=True, null=True, default=None)
    show = models.BooleanField('Показывать', default=True)

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.name


class FieldType(models.Model):
    name = models.CharField('Название', max_length=32, unique=True)
    description = models.CharField('Описание', max_length=32, unique=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Тип особенности'
        verbose_name_plural = 'Типы особенности'

    def __str__(self):
        return self.name


class FieldValue(models.Model):
    field_type = models.ForeignKey(FieldType)
    value_text = models.CharField('Значение (текст)', max_length=32, blank=True, null=True, default=None)
    value_bool = models.BooleanField('Значение (да/нет)', blank=True, default=None)

    class Meta:
        verbose_name = 'Значение особенности'
        verbose_name_plural = 'Значения особенностей'

    def __str__(self):
        val = self.value_text or self.value_bool
        return '{field_type}: {val}'.format(field_type = self.field_type, val=val)


class AnimalDescription(models.Model):
    animal = models.ForeignKey(Animal)
    description = models.TextField('Описание', blank=True, default=None)
    fields = models.ManyToManyField(FieldValue)

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'

    def __str__(self):
        return 'Описание: {}'.format(self.animal)


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')
    image_url = models.URLField('URL изображения')
    animal = models.ForeignKey(Animal)
    width = models.IntegerField('Ширина', blank=True, default=None)
    height = models.IntegerField('Высота', blank=True, default=None)
