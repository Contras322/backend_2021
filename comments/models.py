from django.db import models
from movies.models import Movie


class Comment(models.Model):
    author_name = models.CharField(max_length=45, verbose_name="Автор")
    text = models.TextField(verbose_name="Комментарий")
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
