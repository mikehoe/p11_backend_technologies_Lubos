from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Genre, Country, Movie, Creator


class MovieAdmin(ModelAdmin):

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        for obj in queryset:
            obj.description = ""

    ordering = ['title_orig']
    list_display = ['id', 'title_orig', 'title_cz', 'released']
    list_display_links = ['id', 'title_orig']
    list_per_page = 20
    list_filter = ['genres', 'countries']
    search_fields = ['title_orig', 'title_cz']
    actions = ['cleanup_description']


# Register your models here.
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Creator)
admin.site.register(Movie, MovieAdmin)
