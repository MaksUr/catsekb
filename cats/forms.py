from django import forms
from django.core.exceptions import ValidationError

from cats.models import Animal, FieldType


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

    def clean(self):
        words = self.cleaned_data.get('field_value')
        field_types = FieldType.objects.all()  # TODO: Ограничить FieldType до тех, на которые ссылаются field_value
        for field_type in field_types:
            if words.filter(field_type=field_type).count() > 1:
                raise ValidationError({'field_value': ['Свойство может относиться только к одной группе.']})
