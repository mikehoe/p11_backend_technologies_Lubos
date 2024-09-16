from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}), label="Datum narození:", required=False)
    biography = CharField(widget=Textarea, label='Napiš nám něco o sobě.', required=False)

    @atomic
    def save(self, commit=True):  # commit=True => pokud chceme vytvořené User a Profile zároveň uložit do databáze
        self.instance.is_active = True  # stejné jako self.cleaned_data['is_active'] = True
        user = super().save(commit)  # creates instance of User (Vytvoříme uživetele)
        date_of_birth = self.cleaned_data['date_of_birth']
        biography = self.cleaned_data['biography']
        profile = Profile(user=user,
                          date_of_birth=date_of_birth,
                          biography=biography)
        if commit:
            profile.save()
        return user
