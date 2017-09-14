from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType, FieldValue
from cats.time import get_date_from_age, calc_age_uptoday

DAYS = 'Дней'
MONTHS = 'Месяцев'
YEARS = 'Лет'


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
        label=YEARS,
    )
    months = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(12),
        required=False,
        label=MONTHS
    )
    days = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(31),
        required=False,
        label=DAYS
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance and getattr(instance, 'date_of_birth', None):
            upd = dict()
            upd['initial'] = calc_age_uptoday(before_date=instance.date_of_birth, later_date=date.today())
            kwargs.update(upd)
        forms.ModelForm.__init__(self, *args, **kwargs)

    class Meta:
        model = Animal
        fields = ['name', 'group', 'show', 'field_value', 'sex', 'years', 'months', 'days', 'date_of_birth']

    def clean(self):
        if 'name' in self.changed_data:
            self.check_name()

        if 'field_value' in self.changed_data:
            self.check_field_value()

        if 'date_of_birth' in self.changed_data:
            if not self.cleaned_data['date_of_birth']:
                self.instance.birthday_precision = None
            else:
                self.instance.birthday_precision = Animal.BIRTHDAY_PRECISION_D
        elif any((item in ('years', 'months', 'days')) for item in self.changed_data):
            self.save_date_of_birth_from_age()

    def save_date_of_birth_from_age(self):
        years = self.cleaned_data.get('years')
        months = self.cleaned_data.get('months')
        days = self.cleaned_data.get('days')
        if all(item == '' for item in (years, months, days)):
            self.instance.birthday_precision = None
            self.cleaned_data['date_of_birth'] = None
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
        self.cleaned_data['date_of_birth'] = date_of_birth

    def check_field_value(self):
        words = self.cleaned_data.get('field_value')
        types = set()
        errors = set()
        for w in words:
            if w.field_type in types:
                message = 'Группа "{type}" имеет более одного значения.'.format(type=w.field_type)
                errors.add(message)
            types.add(w.field_type)
        if len(errors):
            raise ValidationError({'field_value': list(errors)})

    def check_name(self):
        name = self.cleaned_data.get('name', None)
        if self.instance.name == name:
            pass
        elif Animal.objects.filter(name=name).exists():
            message = '"{name}" уже сущесвтует'.format(name=name)
            raise ValidationError({'name': [message]})
