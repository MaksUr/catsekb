from django.contrib import admin

# Register your models here.
from django.http import HttpRequest
from django.urls import reverse

from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_FIELD_VALUE, ANIMAL_SEX, ANIMAL_DATE_OF_BIRTH, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, ANIMAL_ANIMAL_LINK
from cats.forms import AnimalForm
from cats.models import Animal, AnimalDescription, AnimalImage, FieldValue, Group, FieldType

DJ_ID = 'id'


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription
    classes = [DJ_CLASSES_COLLAPSE]
    # TODO: form = AnimalDescriptionForm


class ImageInline(admin.StackedInline):
    model = AnimalImage
    classes = [DJ_CLASSES_COLLAPSE]
    # TODO: form = AnimalImageForm


class AnimalAdmin(admin.ModelAdmin):

    def get_absolute_url(self, obj):
        # TODO: create link to site related object
        # l = reverse('animal', args=(obj.id,))
        # l = 'animal_{n}'.format(n=obj.id)
        # res = HttpRequest.build_absolute_uri()
        return 'res'

    list_display = (ANIMAL_NAME, DJ_ID)
    fieldsets = (
        (
            ANIMAL_MAIN_FIELD_SET, {
                DJ_FIELDS: (
                    ANIMAL_NAME, ANIMAL_GROUP, ANIMAL_FIELD_VALUE, ANIMAL_SEX,
                    ANIMAL_CREATED, ANIMAL_UPDATED, 'get_absolute_url'
                ),
            },
        ),
        (
            ANIMAL_AGE_FIELD_SET, {
                DJ_FIELDS: (
                    (ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS),
                    ANIMAL_DATE_OF_BIRTH,
                    ANIMAL_BIRTHDAY_PRECISION
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
    )
    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, 'get_absolute_url')
    form = AnimalForm
    inlines = [AnimalDescriptionInline, ImageInline]


admin.site.register(Animal, AnimalAdmin)


class AnimalsInline(admin.TabularInline):
    extra = 0
    model = Animal


class GroupAdmin(admin.ModelAdmin):
    inlines = [AnimalsInline]
admin.site.register(Group, GroupAdmin)


class FieldValueInline(admin.StackedInline):
    model = FieldValue
    extra = 0


class FieldTypeAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
admin.site.register(FieldType, FieldTypeAdmin)

admin.site.register(AnimalImage)
