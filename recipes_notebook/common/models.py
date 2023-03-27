from django.contrib.auth import get_user_model
from django.db import models

from recipes_notebook.recipes.models import Recipe

UserModel = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
