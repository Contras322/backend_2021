from django.urls import path
from movies.views import add_movie, show_movies, show_current_movie
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add/', add_movie, name='add'),
    path('show_movies/', show_movies, name='show_movies'),
    path('show_current_movie/<int:rating>/', show_current_movie, name='show_current_movie')
]