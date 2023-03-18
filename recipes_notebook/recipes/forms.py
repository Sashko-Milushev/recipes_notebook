from django import forms

from recipes_notebook.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_picture', 'description', 'ingredients']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'ingredients': forms.Textarea(attrs={'rows': 5}),
        }
        help_texts = {
            'ingredients': 'Please separate each ingredient with a comma (e.g. 1 cup sugar, 2 tbsp salt, etc.)',
        }
