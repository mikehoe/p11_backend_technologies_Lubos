from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import Movie, Creator


def home(request):
    return render(request, 'home.html')


def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies': movies_list}
    return render(request, 'movies.html', context)


def creators(request):
    creators_list = Creator.objects.all()
    context = {'creators': creators_list}
    return render(request, 'creators.html', context)
