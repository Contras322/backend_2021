from django.db import models
from django.urls import reverse
from genres.models import Genre


class Movie(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название фильма")
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL, verbose_name="Жанр")
    rating = models.FloatField(null=True, verbose_name="Рейтинг фильма")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_current_movie', kwargs={'movie_id': self.id})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
