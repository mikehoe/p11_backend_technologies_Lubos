from datetime import date

from django.db.models import Model, CharField, DateField, ForeignKey, SET_NULL, TextField, ManyToManyField, \
    IntegerField, FloatField, DateTimeField

# Create your models here.
""" Models
Genre
- name: string

Country
- name: string
- code: string

Creator
- name: string
- surname: string
# - sex ???
- date_of_birth: Date
- date_of_death: Date
#- place_of_birth: string
- country_of_birth -> Country
#- place_of_death: string
- country_of_death -> Country
- biography: string
# - images ???
# - acting -> n:m -> Movie
# - directing -> n:m -> Movie

Movie
- title_orig: string
- title_cz: string  # TODO: titles: list 
- genres -> List[Genre]
- countries -> List[Country]
- actors -> List[Creator]
- directors -> List[Creator]
# TODO: Music, Script...
- length: int (min)
- released: int (year)
- description: string
- rating: float
# - images ???
- created: DateTime
- updated: DateTime

Review
- user -> Profile  # TODO: Profile -> User (Django)
- movie -> Movie
- review: string
- rating: int (0-100)
"""


class Genre(Model):
    name = CharField(max_length=20, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']  # ascending
        # ordering = ['-name']  # descending

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Country(Model):
    name = CharField(max_length=64, null=False, blank=False, unique=True)
    code = CharField(max_length=3, null=False, blank=False, unique=True)

    class Meta:
        verbose_name_plural = "Contries"
        ordering = ['name']  # ascending

    def __repr__(self):
        return f"Country(name={self.name}, code={self.code})"

    def __str__(self):
        return f"{self.name}"


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country_of_birth = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators_born')
    country_of_death = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators_died')
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'name']  # ascending

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname}"

    def age(self):
        if self.date_of_birth:
            end_date = date.today()
            if self.date_of_death:
                end_date = self.date_of_death
            return (end_date.year - self.date_of_birth.year -
                    ((end_date.month, end_date.day) < (self.date_of_birth.month, self.date_of_birth.day)))
        return None


class Movie(Model):
    title_orig = CharField(max_length=150, null=False, blank=False)
    title_cz = CharField(max_length=150, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name="movies")
    countries = ManyToManyField(Country, blank=True, related_name="movies")
    actors = ManyToManyField(Creator, blank=True, related_name="acting")
    directors = ManyToManyField(Creator, blank=True, related_name="directing")
    length = IntegerField(null=True, blank=True)  # min
    released = IntegerField(null=True, blank=True)  # year
    description = TextField(null=True, blank=True)
    rating = FloatField(null=True, blank=True)  # 0-100
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig', 'released']  # ascending

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig})"

    def __str__(self):
        return f"{self.title_orig} ({self.released})"

    def length_format(self):
        hours = self.length // 60
        minutes = self.length % 60
        if minutes < 10:
            minutes = f"0{minutes}"
        return f"{hours}h {minutes}min"


# TODO: Review
"""
Review
- user -> Profile  # TODO: Profile -> User (Django)
- movie -> Movie
- review: string
- rating: int(0 - 100)
"""

# TODO: Images
