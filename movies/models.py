from django.db import models
from genres.models import Genre


class Movie(models.Model):
    movie_name = models.CharField(max_length=45, verbose_name="Название фильма")
    genre_name = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL, verbose_name="")

