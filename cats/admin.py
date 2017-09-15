from django.contrib import admin

# Register your models here.
from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED
from cats.forms import AnimalForm
from cats.models import Animal, AnimalDescription, AnimalImage, FieldValue, Group, FieldType


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription
    classes = ['collapse']
    # TODO: form = AnimalDescriptionForm


class ImageInline(admin.StackedInline):
    model = AnimalImage
    classes = ['collapse']
    # TODO: form = AnimalImageForm


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Общая информация', {
                'fields': ('name', 'group', 'field_value', 'sex'),
            },
        ),
        (
            'Настройки возраста', {
                'fields': (('years', 'months', 'days'), 'date_of_birth', 'birthday_precision'),
                'classes': ['collapse']
            },
        ),
    )
    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED)
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
