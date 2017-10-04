from django.contrib import admin

# Register your models here.
from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_FIELD_VALUE, ANIMAL_SEX, ANIMAL_DATE_OF_BIRTH, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, DJ_ID, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION
from cats.forms import AnimalForm
from cats.models import Animal, AnimalImage, FieldValue, Group, FieldType


class ImageInline(admin.StackedInline):
    model = AnimalImage
    classes = [DJ_CLASSES_COLLAPSE]
    # TODO: form = AnimalImageForm


class AnimalAdmin(admin.ModelAdmin):

    list_display = (DJ_ID, ANIMAL_NAME)
    fieldsets = (
        (
            ANIMAL_MAIN_FIELD_SET, {
                DJ_FIELDS: (
                    ANIMAL_NAME, ANIMAL_SHOW, ANIMAL_DESCRIPTION, ANIMAL_GROUP, ANIMAL_FIELD_VALUE, ANIMAL_SEX,
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


class AnimalsInline(admin.TabularInline):
    # TODO: Implement
    extra = 0
    model = Animal
    form = AnimalForm
    fields = (ANIMAL_NAME, ANIMAL_SEX)


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
