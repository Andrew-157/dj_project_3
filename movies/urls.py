from django.views.generic import TemplateView
from django.urls import path

app_name = 'movies'
urlpatterns = [
    path('', TemplateView.as_view(template_name='movies/index.html'), name='index')
]
