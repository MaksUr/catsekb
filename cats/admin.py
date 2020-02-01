from django.contrib import admin
# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from cats.cats_constants import ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED, ANIMAL_NAME, ANIMAL_GROUP, \
    ANIMAL_SEX, ANIMAL_DAYS, ANIMAL_MONTHS, ANIMAL_YEARS, \
    ANIMAL_AGE_FIELD_SET, ANIMAL_SHOW, \
    ANIMAL_DESCRIPTION, GROUP_NAME, GROUP_SHOW, ANIMAL_LOCATION_STATUS, ANIMAL_TAG, ANIMAL_TAG_FIELD_SET, \
    ANIMAL_TAG_DISPLAY, \
    ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, \
    ANIMAL_IMAGE_BACKGROUND_Y_POSITION, ANIMAL_VK_IMPORT_SET, ANIMAL_VK_ALBUM_ID, \
    ANIMAL_VK_ALBUM_URL, \
    ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_KEY_FORM_VK_UPDATE_PHOTO, \
    ANIMAL_IMAGE_PHOTO_ID, ANIMAL_IMAGE_IMAGE_URL_TAG, \
    ANIMAL_IMAGE_IMAGE_SMALL_URL_TAG, ANIMAL_IMAGE_CREATED, ANIMAL_SHELTER_DATE, \
    ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT, ANIMAL_KEY_FORM_VK_UPDATE_INFO_HELP_TEXT, ANIMAL_FORM_VK_UPDATE_INFO, \
    ANIMAL_KEY_FORM_VK_UPDATE_INFO, ANIMAL_VIDEO_FIELD_SET, ANIMAL_VIDEO, \
    ANIMAL_VIDEO_DESCRIPTION, ANIMAL_VIDEO_SHOW, ANIMAL_VIDEO_PUT_TO_INDEX_PAGE
from catsekb.constants import DJ_CLASSES_COLLAPSE, DJ_CLASSES, DJ_ID, CREATED
from cats.forms import AnimalForm, AnimalImageForm, AnimalVideoForm
from cats.models import Animal, AnimalImage, AnimalVideo
from cats.updater import update_images_for_animal

UPDATE_BUTTON = '<a class="button" href="{link}?upd={upd}">Обновить</a><p class="help">{help}</p>'

ANIMAL_IMAGE_FIELDS = (
    'image_thumb',
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
                                'image_thumb',
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
            url=obj.get_instagram_link() or '',
            label=obj.get_hashtag_name() or '—',
            help='Для обновления необходимо сохранить. Убедитесь в корректности ссылки.'
        )
        return mark_safe(res)
    tag_display.short_description = 'Текущий тег'

    def vk_update_photo(self, obj):
        return mark_safe(UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_PHOTO,
            help=ANIMAL_KEY_FORM_VK_UPDATE_PHOTO_HELP_TEXT
        ))
    vk_update_photo.short_description = ANIMAL_KEY_FORM_VK_UPDATE_PHOTO

    def vk_update_info(self, obj):
        return mark_safe(UPDATE_BUTTON.format(
            link=reverse('admin:cats_animal_change', args=(obj.pk,)),
            upd=ANIMAL_FORM_VK_UPDATE_INFO,
            help=ANIMAL_KEY_FORM_VK_UPDATE_INFO_HELP_TEXT
        ))
    vk_update_info.short_description = ANIMAL_KEY_FORM_VK_UPDATE_INFO

    list_display = (DJ_ID, ANIMAL_NAME, 'project', ANIMAL_LOCATION_STATUS, ANIMAL_SEX, ANIMAL_SHOW)
    list_display_links = (ANIMAL_NAME, DJ_ID)
    fieldsets = (
        (
            ANIMAL_VK_IMPORT_SET, {
                'fields': (
                    ANIMAL_FORM_VK_UPDATE_PHOTO,
                    ANIMAL_FORM_VK_UPDATE_INFO,
                    ANIMAL_VK_ALBUM_ID,
                    ANIMAL_VK_ALBUM_URL,
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
        (
            'Общая инфомация', {
                'fields': (
                    ANIMAL_NAME, 'project', ANIMAL_LOCATION_STATUS,
                    ANIMAL_SHELTER_DATE,
                    ANIMAL_SHOW, ANIMAL_DESCRIPTION,
                    ANIMAL_GROUP, ANIMAL_SEX,
                    ANIMAL_CREATED, ANIMAL_UPDATED,
                ),
            },
        ),
        (
            ANIMAL_TAG_FIELD_SET, {
                'fields': (ANIMAL_TAG, ANIMAL_TAG_DISPLAY),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,),
            },
        ),
        (
            ANIMAL_AGE_FIELD_SET, {
                'fields': (
                    (ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS),
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
        (
            ANIMAL_VIDEO_FIELD_SET, {
                'fields': (
                    (ANIMAL_VIDEO,),
                ),
                DJ_CLASSES: (DJ_CLASSES_COLLAPSE,)
            },
        ),
    )

    readonly_fields = (ANIMAL_BIRTHDAY_PRECISION, ANIMAL_CREATED, ANIMAL_UPDATED,
                       ANIMAL_TAG_DISPLAY, ANIMAL_VK_ALBUM_ID,
                       ANIMAL_FORM_VK_UPDATE_PHOTO, ANIMAL_FORM_VK_UPDATE_INFO,)
    search_fields = (ANIMAL_NAME, ANIMAL_DESCRIPTION)
    form = AnimalForm
    inlines = [ImageInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super(AnimalAdmin, self).get_form(request, obj=None, **kwargs)
        upd = request.GET.get('upd')
        if upd and obj and obj.vk_album_id is not None and obj.vk_group_id:
            form.update_form = upd
            if upd == ANIMAL_FORM_VK_UPDATE_PHOTO:
                update_images_for_animal(obj, obj.vk_group_id, obj.vk_album_id)
        return form
admin.site.register(Animal, AnimalAdmin)


class AnimalsInline(admin.StackedInline):
    extra = 0
    model = Animal
    form = AnimalForm
    fields = (ANIMAL_NAME, ANIMAL_SEX, ANIMAL_SHOW, ANIMAL_LOCATION_STATUS)
    show_change_link = True


class AnimalVideoAdmin(admin.ModelAdmin):
    list_display = (ANIMAL_VIDEO_DESCRIPTION, ANIMAL_VIDEO_SHOW, ANIMAL_VIDEO_PUT_TO_INDEX_PAGE,)
    form = AnimalVideoForm
    readonly_fields = (CREATED,)
admin.site.register(AnimalVideo, AnimalVideoAdmin)
