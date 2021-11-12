from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=45, verbose_name="Жанр")