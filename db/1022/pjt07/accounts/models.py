from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField()
    fans = models.ManyToManyField('self', symmetrical=False, related_name='stars')
