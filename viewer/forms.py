from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator


class CreatorForm(Form):
    name = CharField(max_length=32, required=False)
    surname = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    country_of_birth = ModelChoiceField(queryset=Country.objects, required=False)
    country_of_death = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)

    def clean_name(self):
        cleaned_data = super().clean()
        initial = cleaned_data['name']
        print(f"initial name: '{initial}'")
        result = initial
        if initial is not None:
            result = initial.strip()
            print(f"result: '{result}'")
            if len(result):
                result = result.capitalize()
            print(f"result: '{result}'")
        return result

    def clean_date_of_birth(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data['date_of_birth']
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Lze zadávat datum narození pouze v minulosti')
        return date_of_birth

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        surname = cleaned_data['surname']
        if name is None:
            name = ''
        if surname is None:
            surname = ''
        if len(name.strip()) == 0 and len(surname.strip()) == 0:
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')
        # TODO: pokud jsou zadaná data narození a úmrtí, tak datum narození musí být < datum úmrtí


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
        name = self.cleaned_data['name']
        print(f"initial name: '{name}'")
        if name:
            name = name.strip()
            print(f"stripped name: '{name}'")
            names = name.split()
            if len(names):
                names_capitalized = []
                for name in names:
                    names_capitalized.append(name.capitalize())
                    print(f"names_capitalized: '{names_capitalized}'")
                name = ' '.join(names_capitalized)
                print(f"capitalized name: '{name}'")
        return name

    # Validace a úprava pole "surname"
    def clean_surname(self):
        print("Method clean_surname()")
        surname = self.cleaned_data['surname']
        print(f"initial surname: '{surname}'")
        if surname:
            surname = surname.strip()
            print(f"stripped surname: '{surname}'")
            if len(surname):
                surname = surname.capitalize()
                print(f"capitalized surname: '{surname}'")
        return surname

    # Validace data narození
    def clean_date_of_birth(self):
        print("Method clean_date_of_birth()")
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth and date_of_birth >= date.today():
            raise ValidationError('Lze zadávat datum narození pouze v minulosti')
        return date_of_birth

    # Validace data úmrtí
    def clean_date_of_death(self):
        print("Method clean_date_of_death()")
        date_of_death = self.cleaned_data['date_of_death']
        if date_of_death and date_of_death >= date.today():
            raise ValidationError('Lze zadávat datum úmrtí pouze v minulosti')
        return date_of_death

    # Validace na úrovni formuláře
    def clean(self):
        print("Method clean()")
        cleaned_data = super().clean()

        # Ověření, že alespoň jedno z polí "name" nebo "surname" je vyplněné
        name = cleaned_data.get('name', '')
        surname = cleaned_data.get('surname', '')
        if not name:
            name = ''
        if not surname:
            surname = ''
        if not len(name.strip()) and not len(surname.strip()):
            raise ValidationError('Je potřeba zadat jméno nebo příjmení')

        # Ověření, že datum narození je menší než datum úmrtí
        date_of_birth = cleaned_data.get('date_of_birth')
        date_of_death = cleaned_data.get('date_of_death')

        if date_of_birth and date_of_death and date_of_birth >= date_of_death:
            raise ValidationError('Datum narození musí být před datem úmrtí')
