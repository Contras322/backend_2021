from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=45, verbose_name="Жанр")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
