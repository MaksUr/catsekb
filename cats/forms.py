from datetime import date

from django import forms
from django.forms import ValidationError

from cats.cats_constants import ANIMAL_UPDATED, ANIMAL_CREATED, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_KEY_UPDATED_HELP_TEXT, \
    ANIMAL_KEY_CREATED_HELP_TEXT, ANIMAL_KEY_SHOW_HELP_TEXT, \
    ANIMAL_KEY_SEX_HELP_TEXT, ANIMAL_KEY_NAME_HELP_TEXT, \
    ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST, ANIMAL_DAYS, ANIMAL_FORM_KEY_DAYS, ANIMAL_KEY_DAYS_HELP_TEXT, \
    ANIMAL_MONTHS, ANIMAL_FORM_KEY_MONTHS, \
    ANIMAL_KEY_MONTHS_HELP_TEXT, ANIMAL_YEARS, ANIMAL_FORM_KEY_YEARS, ANIMAL_KEY_YEARS_HELP_TEXT, ANIMAL_SEX, \
    ANIMAL_SHOW, ANIMAL_GROUP, ANIMAL_KEY_GROUP_HELP_TEXT, ANIMAL_NAME, ANIMAL_DATE_OF_BIRTH, \
    ANIMAL_KEY_NAME, ANIMAL_KEY_SEX, AGE_DISTANCE_CHOICES, \
    AGE_DISTANCE_KEY, ANIMAL_DESCRIPTION, ANIMAL_KEY_DESCRIPTION_HELP_TEXT, ANIMAL_KEY_LOCATION_STATUS_HELP_TEXT, \
    ANIMAL_LOCATION_STATUS, ANIMAL_SEX_CHOICES, ANIMAL_LOCATION_STATUS_CHOICES, ANIMAL_KEY_LOCATION_STATUS, ANIMAL_TAG, \
    ANIMAL_KEY_TAG_HELP_TEXT, ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT, \
    ANIMAL_IMAGE_KEY_FAVOURITE_HELP_TEXT, ANIMAL_IMAGE_BACKGROUND_Y_POSITION, \
    ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT, ANIMAL_IMAGE_ANIMAL, ANIMAL_IMAGE_KEY_ANIMAL_HELP_TEXT, \
    ANIMAL_VK_ALBUM_ID, \
    ANIMAL_KEY_VK_ALBUM_URL_HELP_TEXT, ANIMAL_KEY_VK_ALBUM_URL, \
    ANIMAL_VK_ALBUM_URL, ANIMAL_VK_ALBUM_URL_WRONG_FORMAT, \
    ANIMAL_IMAGE_CREATED, ANIMAL_IMAGE_KEY_CREATED_HELP_TEXT, \
    ANIMAL_KEY_SHELTER_DATE_HELP_TEXT, ANIMAL_SHELTER_DATE, ANIMAL_VALID_INFO, ANIMAL_KEY_VALID_INFO_HELP_TEXT, \
    ANIMAL_FORM_VK_UPDATE_INFO, SHELTER_DISTANCE_KEY, SHELTER_DISTANCE_CHOICES, SHELTER_DISTANCE, AGE_DISTANCE, \
    ANIMAL_VIDEO, ANIMAL_KEY_VIDEO_HELP_TEXT, ANIMAL_VIDEO_VIDEO_URL, ANIMAL_VIDEO_DESCRIPTION, \
    ANIMAL_VIDEO_KEY_DESCRIPTION_HELP_TEXT, ANIMAL_VIDEO_KEY_VIDEO_URL_HELP_TEXT, \
    ANIMAL_VIDEO_VIDEO_URL_VALIDATION_MESSAGE, ANIMAL_VIDEO_SHOW, ANIMAL_VIDEO_KEY_SHOW_HELP_TEXT, \
    ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE, ANIMAL_VIDEO_PUT_TO_INDEX_PAGE, ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE_HELP_TEXT
from catsekb.constants import DJ_INSTANCE, DJ_INITIAL, VK_GROUP_ID, NO_CHOICE_VALUE, CLASS
from cats.models import Animal, AnimalImage, AnimalVideo
from cats.time import get_date_from_age, calc_age_uptoday

from cats.update_scripts.vk_response_parser import get_animal_kwargs_from_vk_response
from cats.updater import get_vk_album_id_from_url, get_albums_info


def get_range(size):
    res = [(i, str(i)) for i in range(0, size+1)]
    res = [(None, '-')] + res
    return res


def get_int_val(val):
    if val == '' or val is None:
        return 0
    else:
        return int(val)


class AnimalForm(forms.ModelForm):
    # age
    years = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(20),
        required=False,
        label=ANIMAL_FORM_KEY_YEARS,
        help_text=ANIMAL_KEY_YEARS_HELP_TEXT,
    )
    months = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(12),
        required=False,
        label=ANIMAL_FORM_KEY_MONTHS,
        help_text=ANIMAL_KEY_MONTHS_HELP_TEXT,
    )
    days = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(31),
        required=False,
        label=ANIMAL_FORM_KEY_DAYS,
        help_text=ANIMAL_KEY_DAYS_HELP_TEXT,
    )

    # vk_import
    vk_album_url = forms.URLField(label=ANIMAL_KEY_VK_ALBUM_URL,
                                  help_text=ANIMAL_KEY_VK_ALBUM_URL_HELP_TEXT,
                                  required=False)
    update_form = None

    def __init__(self, *args, **kwargs):
        instance = kwargs.get(DJ_INSTANCE)
        if instance:
            upd = dict()
            if getattr(instance, ANIMAL_DATE_OF_BIRTH, None):
                d = calc_age_uptoday(before_date=instance.date_of_birth, later_date=date.today())
                d = self.get_age_by_precision(d, instance.birthday_precision)
                upd.update(d)
            if getattr(instance, ANIMAL_VK_ALBUM_ID, None):
                upd[ANIMAL_VK_ALBUM_URL] = instance.get_vk_album_url()
            if self.update_form:
                upd.update(self.get_initial_update(instance=instance, upd_type=self.update_form))
            if not kwargs.get(DJ_INITIAL):
                kwargs[DJ_INITIAL] = dict()
            kwargs[DJ_INITIAL].update(upd)

        forms.ModelForm.__init__(self, *args, **kwargs)

    @staticmethod
    def get_initial_update(instance, upd_type):
        res = dict()
        if (instance.vk_album_id is not None) and (upd_type == ANIMAL_FORM_VK_UPDATE_INFO):
            response = get_albums_info(album_ids=(instance.vk_album_id,), group_id=VK_GROUP_ID)
            animal_update = get_animal_kwargs_from_vk_response(response)
            if animal_update.get(ANIMAL_DATE_OF_BIRTH):
                d = calc_age_uptoday(before_date=animal_update[ANIMAL_DATE_OF_BIRTH], later_date=date.today())
                d = AnimalForm.get_age_by_precision(d, animal_update.get(ANIMAL_BIRTHDAY_PRECISION))
                animal_update.update(d)
            res.update(animal_update)
        return res

    class Meta:
        model = Animal
        fields = [
            ANIMAL_NAME, ANIMAL_LOCATION_STATUS,
            ANIMAL_GROUP, ANIMAL_SHOW,
            ANIMAL_SEX,
            ANIMAL_YEARS, ANIMAL_MONTHS,
            ANIMAL_DAYS,
            ANIMAL_DESCRIPTION, ANIMAL_TAG, ANIMAL_VK_ALBUM_URL,
            ANIMAL_SHELTER_DATE, ANIMAL_VALID_INFO, ANIMAL_VIDEO,
        ]
        help_texts = {
            ANIMAL_UPDATED: ANIMAL_KEY_UPDATED_HELP_TEXT,
            ANIMAL_CREATED: ANIMAL_KEY_CREATED_HELP_TEXT,
            ANIMAL_SHOW: ANIMAL_KEY_SHOW_HELP_TEXT,
            ANIMAL_SEX: ANIMAL_KEY_SEX_HELP_TEXT,
            ANIMAL_NAME: ANIMAL_KEY_NAME_HELP_TEXT,
            ANIMAL_GROUP: ANIMAL_KEY_GROUP_HELP_TEXT,
            ANIMAL_DESCRIPTION: ANIMAL_KEY_DESCRIPTION_HELP_TEXT,
            ANIMAL_LOCATION_STATUS: ANIMAL_KEY_LOCATION_STATUS_HELP_TEXT,
            ANIMAL_TAG: ANIMAL_KEY_TAG_HELP_TEXT,
            ANIMAL_VK_ALBUM_URL: ANIMAL_KEY_VK_ALBUM_URL_HELP_TEXT,
            ANIMAL_SHELTER_DATE: ANIMAL_KEY_SHELTER_DATE_HELP_TEXT,
            ANIMAL_VALID_INFO: ANIMAL_KEY_VALID_INFO_HELP_TEXT,
            ANIMAL_VIDEO: ANIMAL_KEY_VIDEO_HELP_TEXT,
        }

    def clean(self):
        if ANIMAL_DATE_OF_BIRTH in self.changed_data:
            if not self.cleaned_data[ANIMAL_DATE_OF_BIRTH]:
                self.instance.birthday_precision = None
                self.save_date_of_birth_from_age()
            else:
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_D
        elif any((item in (ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS)) for item in self.changed_data):
            self.save_date_of_birth_from_age()
        # TODO: not save

    def save_date_of_birth_from_age(self):
        years = self.cleaned_data.get(ANIMAL_YEARS)
        months = self.cleaned_data.get(ANIMAL_MONTHS)
        days = self.cleaned_data.get(ANIMAL_DAYS)
        if all(item == '' for item in (years, months, days)):
            self.instance.birthday_precision = None
            self.cleaned_data[ANIMAL_DATE_OF_BIRTH] = None
            return

        if any(item == '' for item in (years, months, days)):
            if days != '':
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_D
            elif months != '':
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_M
            else:
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_Y

        else:  # all(item != '' for item in (years, months, days))
            self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_D

        date_of_birth = get_date_from_age(
            years=get_int_val(years),
            months=get_int_val(months),
            days=get_int_val(days)
        )
        self.instance.date_of_birth = date_of_birth

    @staticmethod
    def get_age_by_precision(d, precision):
        # TODO: use from model
        if not precision or precision == Animal.BIRTHDAY_PRECISION_D:
            return d
        d[ANIMAL_DAYS] = None
        if precision == Animal.BIRTHDAY_PRECISION_M:
            return d
        d[ANIMAL_MONTHS] = None
        if precision == Animal.BIRTHDAY_PRECISION_Y:
            return d
        d[ANIMAL_YEARS] = None
        return d

    def clean_name(self):
        name = self.cleaned_data.get(ANIMAL_NAME, None)
        if name == "" or self.instance.name == name:
            pass
        elif Animal.objects.filter(name=name).exists():
            message = ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST.format(name=name)
            raise ValidationError(message)
        return name

    def clean_vk_album_url(self):
        vk_alb_url = self.cleaned_data.get(ANIMAL_VK_ALBUM_URL)
        if vk_alb_url:
            vk_album_id = get_vk_album_id_from_url(vk_alb_url)
            if vk_album_id is None:
                raise ValidationError(ANIMAL_VK_ALBUM_URL_WRONG_FORMAT)
            self.instance.vk_album_id = vk_album_id
        return vk_alb_url


class FilterForm(forms.Form):

    name = forms.CharField(
        required=False,
        label=ANIMAL_KEY_NAME,
    )

    sex = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={CLASS: ANIMAL_SEX}),
        required=False, choices=ANIMAL_SEX_CHOICES,
        label=ANIMAL_KEY_SEX
    )

    age_distance = forms.ChoiceField(
        label=AGE_DISTANCE_KEY,
        widget=forms.RadioSelect(attrs={CLASS: AGE_DISTANCE}),
        required=False,
        choices=AGE_DISTANCE_CHOICES
    )

    shelter_distance = forms.ChoiceField(
        label=SHELTER_DISTANCE_KEY,
        widget=forms.RadioSelect(attrs={CLASS: SHELTER_DISTANCE}),
        required=False,
        choices=SHELTER_DISTANCE_CHOICES
    )

    location_status = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={CLASS: ANIMAL_LOCATION_STATUS}),
        required=False,
        choices=ANIMAL_LOCATION_STATUS_CHOICES,
        label=ANIMAL_KEY_LOCATION_STATUS
    )


class AnimalImageForm(forms.ModelForm):

    class Meta:
        model = AnimalImage
        fields = [
            ANIMAL_IMAGE_ANIMAL,
            ANIMAL_IMAGE_FAVOURITE,
            ANIMAL_IMAGE_BACKGROUND,
            ANIMAL_IMAGE_BACKGROUND_Y_POSITION,
            ANIMAL_IMAGE_CREATED,
        ]

        help_texts = {
            ANIMAL_IMAGE_ANIMAL: ANIMAL_IMAGE_KEY_ANIMAL_HELP_TEXT,
            ANIMAL_IMAGE_FAVOURITE: ANIMAL_IMAGE_KEY_FAVOURITE_HELP_TEXT,
            ANIMAL_IMAGE_BACKGROUND: ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT,
            ANIMAL_IMAGE_BACKGROUND_Y_POSITION: ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT,
            ANIMAL_IMAGE_CREATED: ANIMAL_IMAGE_KEY_CREATED_HELP_TEXT,
        }

    def clean(self):
        cleaned_data = forms.ModelForm.clean(self)
        return cleaned_data


class AnimalVideoForm(forms.ModelForm):

    class Meta:
        model = AnimalVideo
        fields = [
            ANIMAL_VIDEO_VIDEO_URL,
            ANIMAL_VIDEO_DESCRIPTION,
            ANIMAL_VIDEO_SHOW,
            ANIMAL_VIDEO_PUT_TO_INDEX_PAGE,
        ]

        help_texts = {
            ANIMAL_VIDEO_VIDEO_URL: ANIMAL_VIDEO_KEY_VIDEO_URL_HELP_TEXT,
            ANIMAL_VIDEO_DESCRIPTION: ANIMAL_VIDEO_KEY_DESCRIPTION_HELP_TEXT,
            ANIMAL_VIDEO_SHOW: ANIMAL_VIDEO_KEY_SHOW_HELP_TEXT,
            ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE: ANIMAL_VIDEO_KEY_PUT_TO_INDEX_PAGE_HELP_TEXT,
        }

    def clean_video_url(self):
        if AnimalVideo.get_video_url(self.cleaned_data.get(ANIMAL_VIDEO_VIDEO_URL)):
            return self.cleaned_data.get(ANIMAL_VIDEO_VIDEO_URL)
        else:
            message = ANIMAL_VIDEO_VIDEO_URL_VALIDATION_MESSAGE
            raise ValidationError(message)
