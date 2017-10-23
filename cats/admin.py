from django.contrib import admin

# Register your models here.
from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_FIELD_VALUE, ANIMAL_SEX, ANIMAL_DATE_OF_BIRTH, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, DJ_ID, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION, GROUP_NAME, GROUP_SHOW, ANIMAL_LOCATION_STATUS
from cats.forms import AnimalForm
from cats.models import Animal, AnimalImage, FieldValue, Group, FieldType, Article


class ImageInline(admin.StackedInline):
    extra = 0
    model = AnimalImage
    classes = [DJ_CLASSES_COLLAPSE]
    # list_display = (...) TODO: implement
    fields = ('image_url', 'image_thumb', 'alt', 'width', 'height', 'favourite')
    readonly_fields = ('alt', 'width', 'height', 'image_thumb')
    # TODO: form = AnimalImageForm


class AnimalAdmin(admin.ModelAdmin):

    list_display = (DJ_ID, ANIMAL_NAME, ANIMAL_LOCATION_STATUS, 'sex', ANIMAL_SHOW)  # TODO: from constants
    fieldsets = (
        (
            ANIMAL_MAIN_FIELD_SET, {
                DJ_FIELDS: (
                    ANIMAL_NAME, ANIMAL_LOCATION_STATUS,
                    ANIMAL_SHOW, ANIMAL_DESCRIPTION,
                    ANIMAL_GROUP, ANIMAL_FIELD_VALUE, ANIMAL_SEX,
                    ANIMAL_CREATED, ANIMAL_UPDATED,
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
                # DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
    )

    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED,)
    form = AnimalForm
    inlines = [ImageInline]


admin.site.register(Animal, AnimalAdmin)


class AnimalsInline(admin.StackedInline):
    extra = 0
    model = Animal
    form = AnimalForm
    fields = (ANIMAL_NAME, ANIMAL_SEX, ANIMAL_SHOW, ANIMAL_LOCATION_STATUS)
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_display = (GROUP_NAME, GROUP_SHOW)
    inlines = [AnimalsInline]
admin.site.register(Group, GroupAdmin)


class FieldValueInline(admin.StackedInline):
    model = FieldValue
    extra = 0


class FieldTypeAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
admin.site.register(FieldType, FieldTypeAdmin)

admin.site.register(AnimalImage)


class ArticleAdmin(admin.ModelAdmin):
    model = Article
admin.site.register(Article, ArticleAdmin)
