from django.contrib import admin
# Register your models here.
from django.urls import reverse

from cats.cats_constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_SEX, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, DJ_ID, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION, GROUP_NAME, GROUP_SHOW, ANIMAL_LOCATION_STATUS, ANIMAL_TAG, ANIMAL_TAG_FIELD_SET, \
    ANIMAL_TAG_DISPLAY, ANIMAL_KEY_TAG_DISPLAY, ANIMAL_IMAGE_IMAGE_THUMB, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, \
    ANIMAL_IMAGE_BACKGROUND_Y_POSITION, ANIMAL_VK_IMPORT_SET, ANIMAL_VK_ALBUM_ID, \
    ANIMAL_VK_ALBUM_URL, \
    ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_KEY_FORM_VK_UPDATE_PHOTO, \
    ANIMAL_IMAGE_PHOTO_ID, ANIMAL_IMAGE_IMAGE_URL_TAG, \
    ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG, ANIMAL_IMAGE_CREATED, ANIMAL_SHELTER_DATE, ANIMAL_VALID_INFO, \
    ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT, ANIMAL_KEY_FORM_VK_UPDATE_INFO_HELP_TEXT, ANIMAL_FORM_VK_UPDATE_INFO, \
    ANIMAL_KEY_FORM_VK_UPDATE_INFO, ANIMAL_KEY_TAG_DISPLAY_HELP_TEXT
from cats.forms import AnimalForm, AnimalImageForm
from cats.models import Animal, AnimalImage, Group
from cats.updater import update_images_for_animal

UPDATE_BUTTON = '<a class="button" href="{link}?upd={upd}">Обновить</a><p class="help">{help}</p>'

ANIMAL_IMAGE_FIELDS = (
        ANIMAL_IMAGE_IMAGE_THUMB,
        ANIMAL_IMAGE_IMAGE_URL_TAG,
        ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG,
        ANIMAL_IMAGE_FAVOURITE,
        ANIMAL_IMAGE_BACKGROUND,
        ANIMAL_IMAGE_BACKGROUND_Y_POSITION,
        ANIMAL_IMAGE_PHOTO_ID,
        ANIMAL_IMAGE_CREATED,
    )

ANIMAL_IMAGE_READONLY_FIELDS = (ANIMAL_IMAGE_IMAGE_URL_TAG,
                                ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG,
                                ANIMAL_IMAGE_IMAGE_THUMB,
                                ANIMAL_IMAGE_PHOTO_ID
                                )


class ImageInline(admin.StackedInline):
    extra = 0
    model = AnimalImage
    form = AnimalImageForm
    classes = [DJ_CLASSES_COLLAPSE]
    fields = ANIMAL_IMAGE_FIELDS
    readonly_fields = ANIMAL_IMAGE_READONLY_FIELDS

    def has_add_permission(self, request):
        return False


class AnimalAdmin(admin.ModelAdmin):
    def tag_display(self, obj):
        res = '<a href="{url}">{label}</a><p class="help">{help}</p>'.format(
            url=obj.get_instagram_link(),
            label=obj.get_hashtag_name(),
            help=ANIMAL_KEY_TAG_DISPLAY_HELP_TEXT
        )
        return res
    tag_display.allow_tags = True
    tag_display.short_description = ANIMAL_KEY_TAG_DISPLAY

    def vk_update_photo(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_PHOTO,
            help=ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT
        )
    vk_update_photo.short_description = ANIMAL_KEY_FORM_VK_UPDATE_PHOTO
    vk_update_photo.allow_tags = True

    def vk_update_info(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_INFO,
            help=ANIMAL_KEY_FORM_VK_UPDATE_INFO_HELP_TEXT
        )
    vk_update_info.short_description = ANIMAL_KEY_FORM_VK_UPDATE_INFO
    vk_update_info.allow_tags = True

    list_display = (DJ_ID, ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX, ANIMAL_SHOW, ANIMAL_VALID_INFO)
    list_display_links = (ANIMAL_NAME, DJ_ID)
    fieldsets = (
        (
            ANIMAL_VK_IMPORT_SET, {
                DJ_FIELDS: (
                    ANIMAL_FORM_VK_UPDATE_PHOTO,
                    ANIMAL_FORM_VK_UPDATE_INFO,
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
                    ANIMAL_SHELTER_DATE,
                    ANIMAL_SHOW, ANIMAL_DESCRIPTION, ANIMAL_VALID_INFO,
                    ANIMAL_GROUP, ANIMAL_SEX,
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
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
    )

    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED,
                       ANIMAL_TAG_DISPLAY, ANIMAL_VK_ALBUM_ID,
                       ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_FORM_VK_UPDATE_INFO,)
    form = AnimalForm
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super(AnimalAdmin, self).get_form(request, obj=None, **kwargs)
        upd = request.GET.get('upd')
        if upd and obj and obj.vk_album_id is not None:
            form.update_form = upd
            if upd == ANIMAL_FORM_VK_UPDATE_PHOTO:
                update_images_for_animal(obj, obj.vk_album_id)
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


class AnimalImageAdmin(admin.ModelAdmin):
    form = AnimalImageForm
    fields = ANIMAL_IMAGE_FIELDS
    readonly_fields = ANIMAL_IMAGE_READONLY_FIELDS
admin.site.register(AnimalImage, AnimalImageAdmin)
