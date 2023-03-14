from django.urls import path

urlpatterns = (
    path('', ListAllRecipes.as_view(), name='list recipes'),
)