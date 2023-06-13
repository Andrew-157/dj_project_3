from django.views.generic import TemplateView
from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('genres/<str:slug>/',
         views.MoviesByGenreListView.as_view(), name='genre-movies'),
    path('movies/<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('directors/<str:slug>/',
         views.DirectorPageView.as_view(), name='director-page'),
    path('actors/<str:slug>/', views.ActorPageView.as_view(), name='actor-page')
]
