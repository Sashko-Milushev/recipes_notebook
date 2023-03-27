from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.views.decorators.csrf import csrf_exempt

from recipes_notebook.common.models import Like
from recipes_notebook.recipes.models import Recipe

UserModel = get_user_model()


class HomeView(views.TemplateView):
    template_name = 'base/home-page.html'


class DashboardView(views.ListView):
    model = Recipe
    template_name = 'recipes/dashboard.html'
    context_object_name = 'recipes'


@method_decorator(csrf_exempt, name='dispatch')
class LikeRecipeView(views.View):
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, recipe=recipe)
        if created:
            likes_count = recipe.likes.count()
        else:
            like.delete()
            likes_count = recipe.likes.count()
        return JsonResponse({'likes_count': likes_count})
