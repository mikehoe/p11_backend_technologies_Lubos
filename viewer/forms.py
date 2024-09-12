from datetime import date

from django.core.exceptions import ValidationError
from django.forms import DateField, ModelForm, NumberInput

from viewer.models import Creator


class CreatorModelForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        # fields = ['surname', 'name', 'date_of_birth', 'date_of_death']
        # exclude = ['date_of_death', 'name']

    date_of_death = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))
    date_of_birth = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

    # Validace a úprava pole "name"
    def clean_name(self):
        print("Method clean_name()")
        name = self.cleaned_data.get('name', '')  # Použití .get() s výchozí hodnotou
        if name:
            name = ' '.join([n.capitalize() for n in name.strip().split()])
        else:
            name = ''
        print(f"capitalized name: '{name}'")
        return name

    # Validace a úprava pole "surname"
    def clean_surname(self):
        print("Method clean_surname()")
        surname = self.cleaned_data.get('surname', '')  # Použití .get() s výchozí hodnotou
        if surname:
            surname = surname.strip().capitalize()
        else:
            surname = ''
        print(f"capitalized surname: '{surname}'")
        return surname

    # Validace data narození, nemusí vracet nic, když neupravuje data
    def clean_date_of_birth(self):
        print("Method clean_date_of_birth()")
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Lze zadávat datum narození pouze v minulosti')
        return date_of_birth

    # Validace data úmrtí, nemusí vracet nic, když neupravuje data
    def clean_date_of_death(self):
        print("Method clean_date_of_death()")
        date_of_death = self.cleaned_data.get('date_of_death')
        if date_of_death and date_of_death >= date.today():
            raise ValidationError('Lze zadávat datum úmrtí pouze v minulosti')
        return date_of_death

    # Validace na úrovni formuláře, nemusí vracet nic, když neupravuje data
    def clean(self):
        print("Method clean()")
        cleaned_data = super().clean()

        # Ověření, že alespoň jedno z polí "name" nebo "surname" je vyplněné
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')

        if not name and not surname:
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')

        # Ověření, že datum narození je menší než datum úmrtí
        date_of_birth = cleaned_data.get('date_of_birth')
        date_of_death = cleaned_data.get('date_of_death')

        if date_of_birth and date_of_death and date_of_birth >= date_of_death:
            raise ValidationError('Datum narození musí být před datem úmrtí')

        return cleaned_data
