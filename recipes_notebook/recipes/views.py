from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from recipes_notebook.recipes.forms import RecipeForm
from recipes_notebook.recipes.models import Recipe


@login_required
def create_recipe(request):
    button_text = 'Create Recipe'
    if request.method == 'GET':
        form = RecipeForm()

    else:
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, 'Recipe created successfully!')
            return redirect('home')

    context = {
        'form': form,
        'button_text': button_text,
    }

    return render(request, 'recipes/create-recipe.html', context)


class RecipeDetailView(views.DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'
