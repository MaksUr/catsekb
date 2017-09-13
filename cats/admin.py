from django.contrib import admin

# Register your models here.
from cats.forms import AnimalForm, AnimalAgeForm
from cats.models import Animal, AnimalDescription, AnimalImage, FieldValue, Group, FieldType, AnimalAge


class AnimalAgeInline(admin.TabularInline):
    model = AnimalAge
    form = AnimalAgeForm


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription


class ImageInline(admin.StackedInline):
    model = AnimalImage


class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    form = AnimalForm
    inlines = [AnimalAgeInline, AnimalDescriptionInline, ImageInline]
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
