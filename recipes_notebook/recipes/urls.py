from django.urls import path

from recipes_notebook.recipes.views import create_recipe

urlpatterns = (
    # path('', ListAllRecipes.as_view(), name='list recipes'),
    path('create/', create_recipe, name='create recipe'),
)