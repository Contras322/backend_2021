from django.urls import path
from movies.views import movies, show_movies, show_current_movie
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('movie/', movies, name='movies'),
    path('show_movies/', show_movies, name='show_movies'),
    path('show_current_movie/<int:movie>/', show_current_movie, name='show_current_movie')
]