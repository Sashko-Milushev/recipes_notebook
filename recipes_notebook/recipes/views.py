from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic as views

from recipes_notebook.common.forms import CommentForm
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


class RecipeDetailView(LoginRequiredMixin, views.DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'
    context_object_name = 'recipe'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        ingredients_list = recipe.ingredients.split(', ')
        comment_form = CommentForm()
        context['likes'] = recipe.likes.all()
        context['comments'] = recipe.comments.all()
        context['ingredients_list'] = ingredients_list
        context['comment_form'] = comment_form

        return context

    def post(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment was added successfully.')
        else:
            messages.error(request, 'There was an error adding your comment.')

        return self.get(request, *args, **kwargs)


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