from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from recipes_notebook.recipes.forms import RecipeForm, RecipeDeleteForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        ingredients_list = recipe.ingredients.split(', ')
        context['likes'] = recipe.likes.all()
        context['comments'] = recipe.comments.all()
        context['ingredients_list'] = ingredients_list
        return context


def update_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'pk': pk,
        'recipe': recipe
    }

    return render(request, 'recipes/update-recipe.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST or None, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'pk': pk,
        'recipe': recipe
    }

    return redirect(request, 'recipes/delete-recipe', context)