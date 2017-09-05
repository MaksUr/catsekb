from django.contrib import admin

# Register your models here.
from cats.forms import AnimalForm
from cats.models import Animal, AnimalDescription, AnimalImage, FieldValue, Group, FieldType


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription


class ImageInline(admin.StackedInline):
    model = AnimalImage


class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForm
    inlines = [AnimalDescriptionInline, ImageInline]
admin.site.register(Animal, AnimalAdmin)


class GroupAdmin(admin.ModelAdmin):
    model = Group
    # TODO: add animal list
admin.site.register(Group, GroupAdmin)


class FieldValueInline(admin.StackedInline):
    model = FieldValue
    extra = 0


class FieldTypeAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
admin.site.register(FieldType, FieldTypeAdmin)

admin.site.register(AnimalImage)
