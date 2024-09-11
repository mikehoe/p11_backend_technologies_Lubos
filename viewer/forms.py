from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea

from viewer.models import Country


class CreatorForm(Form):
    name = CharField(max_length=32, required=False)
    surname = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    country_of_birth = ModelChoiceField(queryset=Country.objects, required=False)
    country_of_death = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)

    def clean_name(self):
        initial = self.cleaned_data['name']
        print(f"initial name: '{initial}'")
        result = initial.strip()
        print(f"result: '{result}'")
        if len(result):
            result = result.capitalize()
        print(f"result: '{result}'")
        return result

    def validate_date_of_birth(self, value):
        super().clean()
        #super().validate(value)
        if value and value >= date.today():
            raise ValidationError('Lze zadávat datum narození pouze v minulosti')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        surname = cleaned_data['surname']
        if len(name.strip()) == 0 and len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')
        # TODO: pokud jsou zadaná data narození a úmrtí, tak datum narození musí být < datum úmrtí
