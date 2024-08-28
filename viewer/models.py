from django.db import models
from django.db.models import Model, CharField, ForeignKey, IntegerField, DateField, DO_NOTHING
from django.db.models.fields import TextField, DateTimeField, AutoField
from django.views.generic import RedirectView


# Create your models here.

class Genre(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Award(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)


class Country(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    code = CharField(max_length=128)


class Person(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    sex = CharField(max_length=128)
    date_of_birth = DateField()
    date_of_death = DateField()
    place_of_birth = CharField(max_length=128)
    place_of_death = CharField(max_length=128)
    nationality = Country
    biography = TextField()


class UserProfile(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=128)
    surname = CharField(max_length=128)
    sex = CharField(max_length=128)
    date_of_registration = DateTimeField(auto_now_add=True)
    about_me = TextField()
    country = Country
    reviews: list["Review"]


class Review(Model):
    id = AutoField(primary_key=True)
    review = TextField()
    rating = IntegerField()
    author = ForeignKey(UserProfile, on_delete=DO_NOTHING)
    movie = ForeignKey("Movie", on_delete=DO_NOTHING)


class Movie(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=128)
    other_titles: list[CharField(max_length=128)]
    genre: list[Genre]
    rating = IntegerField()
    released = DateField()
    length = IntegerField()
    description = TextField()
    created = DateField()
    countries = [Country]
    actors: list[Person]
    directors: list[Person]
    scriptwriters: list[Person]
    cameramen: list[Person]
    music_composers: list[Person]
    awards: list[Award]
