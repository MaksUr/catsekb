from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType, FieldValue


def get_range(size):
    res = [(i, str(i)) for i in range(0, size+1)]
    return [(None, '')] + res


class AnimalForm(forms.ModelForm):
    years = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(20),
        required=False,
        label='Лет'
    )
    months = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(12),
        required=False,
        label='Месяцев'
    )
    days = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(31),
        required=False,
        label='Дней'
    )

    class Meta:
        model = Animal
        fields = ['name', 'group', 'show', 'field_value']

    def clean(self):
        self.check_name()
        self.check_field_value()
        self.save_date_of_birth()

    def save_date_of_birth(self):
        # TODO: implement
        pass

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
