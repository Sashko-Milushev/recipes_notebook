from django.contrib.auth.models import AbstractUser
from django.db import models



class AppUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'
