from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType, FieldValue, AnimalAge


def get_range(size):
    res = [(i, str(i)) for i in range(0, size+1)]
    return [(None, '')] + res


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'group', 'show', 'field_value']

    def clean(self):
        name = self.cleaned_data.get('name', None)
        if self.instance.name == name:
            pass
        elif Animal.objects.filter(name=name).exists():
            message = '"{name}" уже сущесвтует'.format(name=name)
            raise ValidationError({'name': [message]})

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


class AnimalAgeForm(forms.ModelForm):
    years = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(20),
    )
    months = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(12),
    )
    days = forms.ChoiceField(
        widget=forms.Select,
        choices=get_range(31),
    )

    class Meta:
        model = AnimalAge
        fields = ['years', 'months', 'days']

