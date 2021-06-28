from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telegram_handle = models.CharField(max_length=50)
    