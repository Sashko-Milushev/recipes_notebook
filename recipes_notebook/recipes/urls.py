from django.urls import path, include

from recipes_notebook.common.views import LikeRecipeView
from recipes_notebook.recipes.views import create_recipe, RecipeDetailView, update_recipe, delete_recipe

urlpatterns = (
    path('create/', create_recipe, name='create recipe'),
    path('<int:pk>/', include([
        path('', RecipeDetailView.as_view(), name='recipe details'),
        path('update/', update_recipe, name='update recipe'),
        path('delete/', delete_recipe, name='delete recipe'),
        path('like/', LikeRecipeView.as_view(), name='like')
    ])),

)
