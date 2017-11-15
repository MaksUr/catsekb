from django.contrib import admin
# Register your models here.
from django.urls import reverse

from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_FIELD_VALUE, ANIMAL_SEX, ANIMAL_DATE_OF_BIRTH, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, DJ_ID, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION, GROUP_NAME, GROUP_SHOW, ANIMAL_LOCATION_STATUS, ANIMAL_TAG, ANIMAL_TAG_FIELD_SET, \
    ANIMAL_TAG_DISPLAY, ANIMAL_KEY_TAG_DISPLAY, ANIMAL_IMAGE_IMAGE_URL, ANIMAL_IMAGE_IMAGE_THUMB, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_WIDTH, ANIMAL_IMAGE_HEIGHT, \
    ANIMAL_IMAGE_BACKGROUND_Y_POSITION, ANIMAL_IMAGE_ANIMAL, ANIMAL_VK_IMPORT_SET, ANIMAL_VK_ALBUM_ID, \
    ANIMAL_VK_ALBUM_URL, ANIMAL_KEY_FORM_VK_UPDATE, ANIMAL_KEY_TAG_DISPLAY_HELP_TEXT, ANIMAL_FORM_VK_UPDATE, \
    ANIMAL_FORM_VK_UPDATE_DESCR, ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_KEY_FORM_VK_UPDATE_PHOTO, \
    ANIMAL_KEY_FORM_VK_UPDATE_DESCR
from cats.forms import AnimalForm, AnimalImageForm
from cats.models import Animal, AnimalImage, FieldValue, Group, FieldType, Article
from cats.vk_api.vk_import import add_images_from_album

UPDATE_BUTTON = '<a class="button" href="{link}?upd={upd}">Обновить</a>'


class ImageInline(admin.StackedInline):
    extra = 0
    model = AnimalImage
    form = AnimalImageForm
    classes = [DJ_CLASSES_COLLAPSE]
    # list_display = (...) TODO: implement
    fields = (
        ANIMAL_IMAGE_IMAGE_URL,
        ANIMAL_IMAGE_IMAGE_THUMB,
        ANIMAL_IMAGE_FAVOURITE,
        ANIMAL_IMAGE_BACKGROUND,
        ANIMAL_IMAGE_BACKGROUND_Y_POSITION,
        ANIMAL_IMAGE_WIDTH,
        ANIMAL_IMAGE_HEIGHT,
    )
    readonly_fields = (ANIMAL_IMAGE_WIDTH,
                       ANIMAL_IMAGE_HEIGHT,
                       ANIMAL_IMAGE_IMAGE_URL,
                       ANIMAL_IMAGE_IMAGE_THUMB)


class AnimalAdmin(admin.ModelAdmin):
    def tag_display(self, obj):
        res = '<a href="{url}">{label}</a>'.format(url=obj.get_instagram_link(), label=obj.get_hashtag_name())
        return res
    tag_display.allow_tags = True
    tag_display.short_description = ANIMAL_KEY_TAG_DISPLAY

    def vk_update(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE
        )
    vk_update.short_description = ANIMAL_KEY_FORM_VK_UPDATE
    vk_update.allow_tags = True

    def vk_update_photo(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_PHOTO
        )
    vk_update_photo.short_description = ANIMAL_KEY_FORM_VK_UPDATE_PHOTO
    vk_update_photo.allow_tags = True

    def vk_update_descr(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_DESCR
        )
    vk_update_descr.short_description = ANIMAL_KEY_FORM_VK_UPDATE_DESCR
    vk_update_descr.allow_tags = True

    list_display = (DJ_ID, ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX, ANIMAL_SHOW)
    list_display_links = (ANIMAL_NAME, DJ_ID)
    fieldsets = (
        (
            ANIMAL_VK_IMPORT_SET, {
                DJ_FIELDS: (
                    ANIMAL_FORM_VK_UPDATE,
                    ANIMAL_FORM_VK_UPDATE_PHOTO,
                    ANIMAL_FORM_VK_UPDATE_DESCR,
                    ANIMAL_VK_ALBUM_ID,
                    ANIMAL_VK_ALBUM_URL,
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
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
            ANIMAL_TAG_FIELD_SET, {
                DJ_FIELDS: (ANIMAL_TAG, ANIMAL_TAG_DISPLAY),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,),
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

    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED,
                       ANIMAL_TAG_DISPLAY, ANIMAL_VK_ALBUM_ID,
                       ANIMAL_FORM_VK_UPDATE, ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_FORM_VK_UPDATE_DESCR)
    form = AnimalForm
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super(AnimalAdmin, self).get_form(request, obj=None, **kwargs)
        upd = request.GET.get('upd')
        if upd and obj:
            form.update_form = upd
            if upd in (ANIMAL_FORM_VK_UPDATE, ANIMAL_FORM_VK_UPDATE_PHOTO):
                add_images_from_album(animal=obj)
        else:
            form.update_form = None
        return form

admin.site.register(Animal, AnimalAdmin)


class AnimalsInline(admin.StackedInline):
    extra = 0
    model = Animal
    form = AnimalForm
    fields = (ANIMAL_NAME, ANIMAL_SEX, ANIMAL_SHOW, ANIMAL_LOCATION_STATUS)
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_display = (GROUP_NAME, GROUP_SHOW)
    # TODO: Сделать поддержку просмотра котов группы и добавлять
    # inlines = [AnimalsInline]
admin.site.register(Group, GroupAdmin)


class FieldValueInline(admin.StackedInline):
    model = FieldValue
    extra = 0


class FieldTypeAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
admin.site.register(FieldType, FieldTypeAdmin)


class AnimalImageAdmin(admin.ModelAdmin):
    form = AnimalImageForm
    fields = (
        ANIMAL_IMAGE_ANIMAL,
        ANIMAL_IMAGE_IMAGE_URL,
        ANIMAL_IMAGE_IMAGE_THUMB,
        ANIMAL_IMAGE_FAVOURITE,
        ANIMAL_IMAGE_BACKGROUND,
        ANIMAL_IMAGE_BACKGROUND_Y_POSITION,
        ANIMAL_IMAGE_WIDTH,
        ANIMAL_IMAGE_HEIGHT,
    )
    readonly_fields = (ANIMAL_IMAGE_WIDTH,
                       ANIMAL_IMAGE_HEIGHT,
                       ANIMAL_IMAGE_IMAGE_URL,
                       ANIMAL_IMAGE_IMAGE_THUMB)
admin.site.register(AnimalImage, AnimalImageAdmin)


class ArticleAdmin(admin.ModelAdmin):
    model = Article
admin.site.register(Article, ArticleAdmin)
