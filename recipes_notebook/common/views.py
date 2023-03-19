from django.shortcuts import render
from django.views import generic as views

from recipes_notebook.recipes.models import Recipe


class HomeView(views.TemplateView):
    template_name = 'base/home-page.html'


class DashboardView(views.ListView):
    model = Recipe
    template_name = 'recipes/recipe-card.html'
    context_object_name = 'recipes'
