from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType, FieldValue


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

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
