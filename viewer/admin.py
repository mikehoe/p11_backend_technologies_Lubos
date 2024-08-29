from django.contrib import admin

from viewer.models import Genre, Country, Movie, Creator

# Register your models here.
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Movie)
admin.site.register(Creator)

