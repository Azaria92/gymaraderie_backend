from django.db import models
from django.contrib.auth.models import AbstractUser


# User model with following field
class User(AbstractUser):
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username
