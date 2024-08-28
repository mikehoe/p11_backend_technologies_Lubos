from django.db import models
from django.db.models import Model, CharField

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
    name = CharField(max_length=20)

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"
