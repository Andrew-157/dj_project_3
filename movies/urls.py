from django.views.generic import TemplateView
from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
