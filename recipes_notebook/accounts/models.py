from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class AppUser(AbstractUser):

    profile_picture = CloudinaryField('image')
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
