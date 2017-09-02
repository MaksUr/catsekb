from django.contrib import admin

# Register your models here.
from cats.models import Animal, AnimalDescription, Image, FieldValue, Group, FieldType


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription


class ImageInline(admin.StackedInline):
    model = Image


class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalDescriptionInline, ImageInline]
admin.site.register(Animal, AnimalAdmin)


class GroupAdmin(admin.ModelAdmin):
    model = Group
admin.site.register(Group, GroupAdmin)


class FieldValueInline(admin.StackedInline):
    model = FieldValue
    extra = 0


class FieldTypeAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
admin.site.register(FieldType, FieldTypeAdmin)
