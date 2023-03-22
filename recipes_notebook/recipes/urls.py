from django.urls import path

from recipes_notebook.recipes.views import create_recipe, RecipeDetailView

urlpatterns = (
    path('create/', create_recipe, name='create recipe'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe details'),
)
