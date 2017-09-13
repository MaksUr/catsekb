from django.contrib import admin

# Register your models here.
from cats.forms import AnimalForm
from cats.models import Animal, AnimalDescription, AnimalImage, FieldValue, Group, FieldType


class AnimalDescriptionInline(admin.StackedInline):
    model = AnimalDescription


class ImageInline(admin.StackedInline):
    model = AnimalImage


class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'date_of_birth')
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
