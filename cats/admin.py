from django.contrib import admin
# Register your models here.
from django.urls import reverse

from cats.constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_FIELD_VALUE, ANIMAL_SEX, ANIMAL_DATE_OF_BIRTH, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_FIELDS, ANIMAL_MAIN_FIELD_SET, DJ_ID, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION, GROUP_NAME, GROUP_SHOW, ANIMAL_LOCATION_STATUS, ANIMAL_TAG, ANIMAL_TAG_FIELD_SET, \
    ANIMAL_TAG_DISPLAY, ANIMAL_KEY_TAG_DISPLAY, ANIMAL_IMAGE_IMAGE_THUMB, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, \
    ANIMAL_IMAGE_BACKGROUND_Y_POSITION, ANIMAL_VK_IMPORT_SET, ANIMAL_VK_ALBUM_ID, \
    ANIMAL_VK_ALBUM_URL, \
    ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_KEY_FORM_VK_UPDATE_PHOTO, \
    ANIMAL_IMAGE_PHOTO_ID, ANIMAL_IMAGE_IMAGE_URL_TAG, \
    ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG, VK_GROUP_ID, ANIMAL_IMAGE_CREATED, ANIMAL_SHELTER_DATE, ANIMAL_VALID_INFO
from cats.forms import AnimalForm, AnimalImageForm
from cats.models import Animal, AnimalImage, FieldValue, Group, FieldType, Article
from cats.updater.vk_request import get_album_photos
# from cats.updater.vk_import import add_images_from_response

UPDATE_BUTTON = '<a class="button" href="{link}?upd={upd}">Обновить</a><p class="help">Help.</p>'

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
        res = '<a href="{url}">{label}</a>'.format(url=obj.get_instagram_link(), label=obj.get_hashtag_name())
        return res
    tag_display.allow_tags = True
    tag_display.short_description = ANIMAL_KEY_TAG_DISPLAY

    def vk_update_photo(self, obj):
        return UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_PHOTO
        )
    vk_update_photo.short_description = ANIMAL_KEY_FORM_VK_UPDATE_PHOTO
    vk_update_photo.allow_tags = True

    list_display = (DJ_ID, ANIMAL_NAME, ANIMAL_LOCATION_STATUS, ANIMAL_SEX, ANIMAL_SHOW, ANIMAL_VALID_INFO)
    list_display_links = (ANIMAL_NAME, DJ_ID)
    fieldsets = (
        (
            ANIMAL_VK_IMPORT_SET, {
                DJ_FIELDS: (
                    ANIMAL_FORM_VK_UPDATE_PHOTO,
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
                       ANIMAL_FORM_VK_UPDATE_PHOTO,)
    form = AnimalForm
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super(AnimalAdmin, self).get_form(request, obj=None, **kwargs)
        upd = request.GET.get('upd')
        if upd and obj and obj.vk_album_id is not None:
            form.update_form = upd
            if upd == ANIMAL_FORM_VK_UPDATE_PHOTO:
                # TODO: Перенести логику обновления в модель
                response = get_album_photos(group_id=VK_GROUP_ID, album_id=obj.vk_album_id)
                add_images_from_response(animal=obj, response=response)
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
    fields = ANIMAL_IMAGE_FIELDS
    readonly_fields = ANIMAL_IMAGE_READONLY_FIELDS
admin.site.register(AnimalImage, AnimalImageAdmin)


class ArticleAdmin(admin.ModelAdmin):
    model = Article
admin.site.register(Article, ArticleAdmin)
