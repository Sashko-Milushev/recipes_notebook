from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from cloudinary.models import CloudinaryField

UserModel = get_user_model()


class Recipe(models.Model):
    RECIPE_TITLE_MAX_LEN = 50
    RECIPE_TITLE_MIN_LEN = 3
    RECIPE_DESCRIPTION_MAX_LEN = 1000
    RECIPE_DESCRIPTION_MIN_LEN = 10
    RECIPE_INGREDIENTS_MAX_LEN = 255
    RECIPE_INGREDIENTS_MIN_LEN = 5

    title = models.CharField(
        verbose_name='Recipe Title',
        max_length=RECIPE_TITLE_MAX_LEN,
        validators=(validators.MinLengthValidator(RECIPE_TITLE_MIN_LEN),),
        blank=False,
        null=False
    )

    recipe_picture = CloudinaryField(
        folder='recipes/',
        blank=False,
        null=False,

    )

    description = models.TextField(
        verbose_name='Recipe Description',
        max_length=RECIPE_DESCRIPTION_MAX_LEN,
        validators=(validators.MinLengthValidator(RECIPE_DESCRIPTION_MIN_LEN),),
        blank=False,
        null=False
    )
    ingredients = models.TextField(
        verbose_name='Recipe ingredients',
        max_length=RECIPE_INGREDIENTS_MAX_LEN,
        validators=(validators.MinLengthValidator(RECIPE_INGREDIENTS_MIN_LEN),),
        blank=False,
        null=False
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    posted_on = models.DateTimeField(
        auto_now_add=True,
    )
