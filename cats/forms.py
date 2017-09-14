from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType, FieldValue
from cats.time import get_date_from_age, calc_age_uptoday

ANIMAL_FORM_VALIDATION_ERROR_NAME_ALREADY_EXIST = '"{name}" уже сущесвтует'

ANIMAL_FORM_VALIDATION_ERROR_MULTIPLY_GROUPS = 'Группа "{type}" имеет более одного значения.'

DJ_INITIAL = 'initial'

ANIMAL_DAYS = 'days'

ANIMAL_MONTHS = 'months'

ANIMAL_YEARS = 'years'

ANIMAL_SEX = 'sex'

ANIMAL_FIELD_VALUE = 'field_value'

ANIMAL_SHOW = 'show'

ANIMAL_GROUP = 'group'

ANIMAL_NAME = 'name'

ANIMAL_DATE_OF_BIRTH = 'date_of_birth'

DJ_INSTANCE = 'instance'

ANIMAL_FORM_KEY_DAYS = 'Дней'
ANIMAL_FORM_KEY_MONTHS = 'Месяцев'
ANIMAL_FORM_KEY_YEARS = 'Лет'


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
    )
    months = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(12),
        required=False,
        label=ANIMAL_FORM_KEY_MONTHS
    )
    days = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(31),
        required=False,
        label=ANIMAL_FORM_KEY_DAYS
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get(DJ_INSTANCE)
        if instance and getattr(instance, ANIMAL_DATE_OF_BIRTH, None):
            upd = dict()
            upd[DJ_INITIAL] = calc_age_uptoday(before_date=instance.date_of_birth, later_date=date.today())
            kwargs.update(upd)
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = Animal
        fields = [
            ANIMAL_NAME, ANIMAL_GROUP, ANIMAL_SHOW,
            ANIMAL_FIELD_VALUE, ANIMAL_SEX,
            ANIMAL_YEARS, ANIMAL_MONTHS,
            ANIMAL_DAYS, ANIMAL_DATE_OF_BIRTH
        ]

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
