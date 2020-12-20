from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age  = models.PositiveSmallIntegerField(blank=True, null=True)
