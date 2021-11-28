from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    location = models.CharField('Город', max_length=45, null=True)
    registration_date = models.DateField('Дата регистрации', null=True)
    email = models.EmailField(max_length=45, unique=True, verbose_name='Электронная почта')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"