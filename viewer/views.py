from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from viewer.forms import CreatorModelForm
from viewer.models import Movie, Creator, Genre, Country

LOGGER = getLogger()


def home(request):
    return render(request, "home.html")


# Class-Based View (CBV)
## ListView class
class MoviesListView(ListView):
    template_name = "movies.html"
    model = Movie
    # pozor: do template se posílají data jako 'object_list'
    # můžeme to přejmenovat:
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        genres = Genre.objects.all()
        context['genres'] = genres
        context['countries'] = Country.objects.all()
        context['movies'] = Movie.objects.all()
        return context


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        # print(movie_)
        return render(request, "movie.html", context)
    return redirect('movies')


class CreatorsListView(ListView):
    template_name = "creators.html"
    model = Creator
    context_object_name = 'creators'


# @login_required
def creator(request, pk):
    if Creator.objects.filter(id=pk).exists():
        creator_ = Creator.objects.get(id=pk)
        return render(request, "creator.html", {'creator': creator_})
    return redirect('creators')


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# Nemusíme psát metodu form_valid(), pokud nijak speciálně neupravujeme (nejlepší je to upravit v clean metodach())
class CreatorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.add_creator'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class CreatorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')
    model = Creator
    permission_required = 'viewer.change_creator'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class CreatorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.delete_creator'


class GenreView(View):
    def get(self, request, pk):
        genres = Genre.objects.all()
        genre = Genre.objects.get(id=pk)
        movies = Movie.objects.filter(genres__id=pk)
        countries = Country.objects.all()
        context = {'genres': genres, 'genre': genre, 'movies': movies,
                   'countries': countries}
        return render(request, "movies.html", context)


class CountryView(View):
    def get(self, request, pk):
        genres = Genre.objects.all()
        countries = Country.objects.all()
        country = Country.objects.get(id=pk)
        movies = Movie.objects.filter(countries=country)
        context = {'genres': genres, 'countries': countries, 'movies': movies, 'country': country}
        return render(request, "movies.html", context)
