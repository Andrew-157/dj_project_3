from django.shortcuts import render
from django.views.generic import ListView
from taggit.models import Tag


class IndexView(ListView):
    template_name = 'movies/index.html'
    context_object_name = 'genres'
    queryset = Tag.objects.order_by('name').all()
