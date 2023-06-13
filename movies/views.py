from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
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
        genre_slug = self.kwargs['genre_slug']
        genre = Tag.objects.filter(slug=genre_slug).first()
        movies = Movie.objects.filter(genres=genre).\
            prefetch_related('genres').\
            select_related('director').all()
        return movies

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['genre'] = self.kwargs['genre_slug']
        return context
