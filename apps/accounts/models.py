from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

