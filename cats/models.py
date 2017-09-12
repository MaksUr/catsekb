from datetime import date
from django.db.models import Model, CharField, TextField, ForeignKey, DateTimeField, BooleanField, ManyToManyField, \
    OneToOneField, ImageField, URLField, IntegerField, DateField

# Create your models here.
from cats.time import calc_age_uptoday


class Group(Model):
    name = CharField('Имя', max_length=32, unique=True)
    description = TextField('Описание', blank=True, default=None)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class FieldType(Model):
    name = CharField('Название', max_length=32, unique=True)
    description = CharField('Описание', max_length=32, blank=True, default=None)

    class Meta:
        verbose_name = 'Тип особенности'
        verbose_name_plural = 'Типы особенностей'

    def __str__(self):
        return self.name


class FieldValue(Model):
    field_type = ForeignKey(FieldType)
    value_text = CharField('Значение (текст)', max_length=32, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Значение особенности'
        verbose_name_plural = 'Значения особенностей'

    def __str__(self):
        val = self.value_text
        return '{field_type}: {val}'.format(field_type=self.field_type, val=val)


class Animal(Model):
    name = CharField('Имя', max_length=32, unique=True, blank=True, default=None)
    # TODO: Create sex field
    created = DateTimeField('Дата публикации', auto_now_add=True, auto_now=False)
    updated = DateTimeField('Дата обновления', auto_now_add=False, auto_now=True)
    date_of_birth = DateField('Возраст', blank=True, null=True, default=None)
    group = ForeignKey(Group, verbose_name=Group._meta.verbose_name, blank=True, null=True, default=None)
    show = BooleanField('Показывать', default=True)
    field_value = ManyToManyField(
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

    def get_age(self):
        if self.date_of_birth:
            return calc_age_uptoday(before_date=self.date_of_birth, later_date=date.today())
        else:
            return None


class AnimalDescription(Model):
    animal = OneToOneField(Animal, unique=True, blank=True, default=None)
    description = TextField('Описание', blank=True, default=None)

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'

    def __str__(self):
        return 'Описание: {}'.format(self.animal)


class AnimalImage(Model):
    animal = OneToOneField(Animal)
    image = ImageField('Изображение', upload_to='images/')
    image_url = URLField('URL изображения', blank=True, default=None)
    alt = CharField('Подпись к фото', max_length=50)
    width = IntegerField('Ширина', blank=True, default=None, null=True)
    height = IntegerField('Высота', blank=True, default=None, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

