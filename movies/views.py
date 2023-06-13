from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from taggit.models import Tag
from movies.models import Movie, Director


class IndexView(ListView):
    template_name = 'movies/index.html'
    context_object_name = 'genres'
    queryset = Tag.objects.order_by('name').all()


class MoviesByGenreListView(ListView):
    template_name = 'movies/movies_by_genre.html'
    context_object_name = 'movies'

    def get_queryset(self) -> QuerySet[Any]:
        genre_slug = self.kwargs['slug']
        genre = Tag.objects.filter(slug=genre_slug).first()
        movies = Movie.objects.filter(genres=genre).\
            prefetch_related('genres').\
            select_related('director').all()
        return movies

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['genre'] = self.kwargs['slug']
        return context


class MovieDetailView(DetailView):
    model = Movie
    queryset = Movie.objects.prefetch_related(
        'genres', 'actors').select_related('director').all()
    template_name = 'movies/movie_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self):
        movie_slug = self.kwargs['slug']
        movie = Movie.objects.filter(slug=movie_slug).first()
        if not movie:
            self.template_name = 'movies/nonexistent.html'
            return None
        return super().get_object()


class DirectorPageView(View):
    template_name = 'movies/director_page.html'

    def get(self, request, *args, **kwargs):
        director_slugged_name = self.kwargs['slug']
        director = Director.objects.filter(
            slugged_name=director_slugged_name).first()
        if not director:
            return render(request, 'movies/nonexistent.html')
        movies = Movie.objects.\
            select_related('director').\
            filter(director=director).all().order_by('title')
        return render(request, self.template_name, {'movies': movies, 'director': director})
