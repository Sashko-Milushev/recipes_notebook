from django import forms

from recipes_notebook.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_picture', 'description', 'ing']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
