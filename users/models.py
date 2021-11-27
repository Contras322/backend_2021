from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    location = models.CharField('Город', max_length=45, null=True)
    registration_date = models.DateField('Дата регистрации', null=True)
