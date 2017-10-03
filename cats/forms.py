from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from cats.constants import ANIMAL_UPDATED, ANIMAL_CREATED, ANIMAL_BIRTHDAY_PRECISION, ANIMAL_KEY_UPDATED_HELP_TEXT, \
    ANIMAL_KEY_CREATED_HELP_TEXT, ANIMAL_KEY_SHOW_HELP_TEXT, ANIMAL_KEY_DATE_OF_BIRTH_HELP_TEXT, \
    ANIMAL_KEY_BIRTHDAY_PRECISION_HELP_TEXT, ANIMAL_KEY_SEX_HELP_TEXT, ANIMAL_KEY_NAME_HELP_TEXT, \
    ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST, ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS, DJ_INSTANCE, \
    DJ_INITIAL, ANIMAL_DAYS, ANIMAL_FORM_KEY_DAYS, ANIMAL_KEY_DAYS_HELP_TEXT, ANIMAL_MONTHS, ANIMAL_FORM_KEY_MONTHS, \
    ANIMAL_KEY_MONTHS_HELP_TEXT, ANIMAL_YEARS, ANIMAL_FORM_KEY_YEARS, ANIMAL_KEY_YEARS_HELP_TEXT, ANIMAL_SEX, \
    ANIMAL_FIELD_VALUE, ANIMAL_SHOW, ANIMAL_GROUP, ANIMAL_KEY_GROUP_HELP_TEXT, ANIMAL_NAME, ANIMAL_DATE_OF_BIRTH, \
    ANIMAL_KEY_FIELD_VALUE_HELP_TEXT
from cats.models import Animal, Group
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
            ANIMAL_NAME,
            ANIMAL_GROUP, ANIMAL_SHOW,
            ANIMAL_FIELD_VALUE, ANIMAL_SEX,
            ANIMAL_YEARS, ANIMAL_MONTHS,
            ANIMAL_DAYS, ANIMAL_DATE_OF_BIRTH
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
        }

    def clean(self):
        if ANIMAL_NAME in self.changed_data:
            self.check_name()

        if ANIMAL_FIELD_VALUE in self.changed_data:
            self.check_field_value()

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

    def check_field_value(self):
        words = self.cleaned_data.get(ANIMAL_FIELD_VALUE)
        types = set()
        errors = set()
        for w in words:
            if w.field_type in types:
                message = ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS.format(type=w.field_type)
                errors.add(message)
            types.add(w.field_type)
        if len(errors):
            raise ValidationError({ANIMAL_FIELD_VALUE: list(errors)})

    def check_name(self):
        name = self.cleaned_data.get(ANIMAL_NAME, None)
        if self.instance.name == name:
            pass
        elif Animal.objects.filter(name=name).exists():
            message = ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST.format(name=name)
            raise ValidationError({ANIMAL_NAME: [message]})


class FilterForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='Имя',
    )
    sex = forms.ChoiceField(widget=forms.RadioSelect, required=False, choices=(('M', 'муж'), ('F', 'жен')), label='Пол')
    age_distance = forms.ChoiceField(
        label='Возрастной промежуток',
        widget=forms.RadioSelect,
        required=False,
        choices=(
            ('_d5', 'до 5 дней'),
            ('d5_m1', 'от 5 дней до меся'),
            ('m1_m6', 'от месяца до полугода'),
            ('m6_y1', 'от полугода до года'),
            ('y1_y2', 'от года до двух'),
            ('y2_y5', 'от двух до пяти лет'),
            ('y5_', 'более пяти лет'),
        )
    )

# TODO: implement class AnimalDescriptionForm


# TODO: implement class AnimalImageForm
