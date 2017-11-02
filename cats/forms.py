from datetime import date

from django import forms
from django.forms import ValidationError

from cats.constants import ANIMAL_UPDATED, ANIMAL_CREATED, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_KEY_UPDATED_HELP_TEXT, \
    ANIMAL_KEY_CREATED_HELP_TEXT, ANIMAL_KEY_SHOW_HELP_TEXT, ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT, \
    ANIMAL_KEY_BIRTHDAY_PRECISION_HELP_TEXT, ANIMAL_KEY_SEX_HELP_TEXT, ANIMAL_KEY_NAME_HELP_TEXT, \
    ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST, ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS, DJ_INSTANCE, \
    DJ_INITIAL, ANIMAL_DAYS, ANIMAL_FORM_KEY_DAYS, ANIMAL_KEY_DAYS_HELP_TEXT, ANIMAL_MONTHS, ANIMAL_FORM_KEY_MONTHS, \
    ANIMAL_KEY_MONTHS_HELP_TEXT, ANIMAL_YEARS, ANIMAL_FORM_KEY_YEARS, ANIMAL_KEY_YEARS_HELP_TEXT, ANIMAL_SEX, \
    ANIMAL_FIELD_VALUE, ANIMAL_SHOW, ANIMAL_GROUP, ANIMAL_KEY_GROUP_HELP_TEXT, ANIMAL_NAME, ANIMAL_DATE_OF_BIRTH, \
    ANIMAL_KEY_FIELD_VALUE_HELP_TEXT, ANIMAL_KEY_NAME, ANIMAL_KEY_SEX, AGE_DISTANCE_CHOICES, \
    AGE_DISTANCE_KEY, ANIMAL_DESCRIPTION, ANIMAL_KEY_DESCRIPTION_HELP_TEXT, ANIMAL_KEY_LOCATION_STATUS_HELP_TEXT, \
    ANIMAL_LOCATION_STATUS, ANIMAL_SEX_CHOICES, ANIMAL_LOCATION_STATUS_CHOICES, ANIMAL_KEY_LOCATION_STATUS, ANIMAL_TAG, \
    ANIMAL_KEY_TAG_HELP_TEXT, ANIMAL_IMAGE_FAVOURITE, ANIMAL_IMAGE_BACKGROUND, ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT, \
    ANIMAL_IMAGE_KEY_FAVOURITE_HELP_TEXT, ANIMAL_IMAGE_BACKGROUND_Y_POSITION, \
    ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT
from cats.models import Animal
from cats.time import get_date_from_age, calc_age_uptoday


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

    def __init__(self, *args, **kwargs):
        instance = kwargs.get(DJ_INSTANCE)
        if instance:
            upd = dict()
            upd[DJ_INITIAL] = dict()
            if getattr(instance, ANIMAL_DATE_OF_BIRTH, None):
                upd[DJ_INITIAL].update(calc_age_uptoday(before_date=instance.date_of_birth, later_date=date.today()))
                kwargs.update(upd)

        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = Animal
        fields = [
            ANIMAL_NAME, ANIMAL_LOCATION_STATUS,
            ANIMAL_GROUP, ANIMAL_SHOW,
            ANIMAL_FIELD_VALUE, ANIMAL_SEX,
            ANIMAL_YEARS, ANIMAL_MONTHS,
            ANIMAL_DAYS, ANIMAL_DATE_OF_BIRTH,
            ANIMAL_DESCRIPTION, ANIMAL_TAG,
        ]
        help_texts = {
            ANIMAL_UPDATED: ANIMAL_KEY_UPDATED_HELP_TEXT,
            ANIMAL_CREATED: ANIMAL_KEY_CREATED_HELP_TEXT,
            ANIMAL_SHOW: ANIMAL_KEY_SHOW_HELP_TEXT,
            ANIMAL_DATE_OF_BIRTH: ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT,
            ANIMAL_BIRTHDAY_PRECISION: ANIMAL_KEY_BIRTHDAY_PRECISION_HELP_TEXT,
            ANIMAL_SEX: ANIMAL_KEY_SEX_HELP_TEXT,
            ANIMAL_NAME: ANIMAL_KEY_NAME_HELP_TEXT,
            ANIMAL_GROUP: ANIMAL_KEY_GROUP_HELP_TEXT,
            ANIMAL_FIELD_VALUE: ANIMAL_KEY_FIELD_VALUE_HELP_TEXT,
            ANIMAL_DESCRIPTION: ANIMAL_KEY_DESCRIPTION_HELP_TEXT,
            ANIMAL_LOCATION_STATUS: ANIMAL_KEY_LOCATION_STATUS_HELP_TEXT,
            ANIMAL_TAG: ANIMAL_KEY_TAG_HELP_TEXT,
        }

    def clean(self):
        if ANIMAL_DATE_OF_BIRTH in self.changed_data:
            if not self.cleaned_data[ANIMAL_DATE_OF_BIRTH]:
                self.instance.birthday_precision = None
            else:
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_D
        elif any((item in (ANIMAL_YEARS, ANIMAL_MONTHS, ANIMAL_DAYS)) for item in self.changed_data):
            self.save_date_of_birth_from_age()

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
        self.cleaned_data[ANIMAL_DATE_OF_BIRTH] = date_of_birth

    def clean_field_value(self):
        words = self.cleaned_data.get(ANIMAL_FIELD_VALUE)
        types = set()
        errors = set()
        for w in words:
            if w.field_type in types:
                message = ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS.format(type=w.field_type)
                errors.add(message)
            types.add(w.field_type)
        if len(errors):
            raise ValidationError(list(errors))
        return words

    def clean_name(self):
        name = self.cleaned_data.get(ANIMAL_NAME, None)
        if name == "" or self.instance.name == name:
            pass
        elif Animal.objects.filter(name=name).exists():
            message = ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST.format(name=name)
            raise ValidationError(message)
        return name


class FilterForm(forms.Form):
    name = forms.CharField(
        required=False,
        label=ANIMAL_KEY_NAME,
    )
    sex = forms.ChoiceField(widget=forms.RadioSelect, required=False, choices=ANIMAL_SEX_CHOICES, label=ANIMAL_KEY_SEX)
    age_distance = forms.ChoiceField(
        label=AGE_DISTANCE_KEY,
        widget=forms.RadioSelect,
        required=False,
        choices=AGE_DISTANCE_CHOICES
    )
    location_status = forms.ChoiceField(
        widget=forms.RadioSelect,
        required=False,
        choices=ANIMAL_LOCATION_STATUS_CHOICES,
        label=ANIMAL_KEY_LOCATION_STATUS
    )

    def __init__(self, *args, **kwargs):
        field_types = kwargs.pop('field_types', dict())
        forms.Form.__init__(self, *args, **kwargs)
        for field_type in field_types:
            t_id = field_type['id']
            choices = field_type['choices']
            label = field_type['label']

            self.fields[t_id] = forms.ChoiceField(
                widget=forms.RadioSelect,
                required=False,
                choices=choices,
                label=label
            )


# TODO: implement class AnimalImageForm
class AnimalImageForm(forms.ModelForm):
    fields = [
        ANIMAL_IMAGE_FAVOURITE,
        ANIMAL_IMAGE_BACKGROUND,
        ANIMAL_IMAGE_BACKGROUND_Y_POSITION,
        # TODO: Форму добавления фото
    ]

    help_texts = {
        ANIMAL_IMAGE_FAVOURITE: ANIMAL_IMAGE_KEY_FAVOURITE_HELP_TEXT,
        ANIMAL_IMAGE_BACKGROUND: ANIMAL_IMAGE_KEY_BACKGROUND_HELP_TEXT,
        ANIMAL_IMAGE_BACKGROUND_Y_POSITION: ANIMAL_IMAGE_KEY_BACKGROUND_Y_POSITION_HELP_TEXT,
    }
