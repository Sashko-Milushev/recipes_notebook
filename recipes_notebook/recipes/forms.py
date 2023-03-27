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


class RecipeDeleteForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['recipe_picture'].disabled = True
        self.fields['description'].disabled = True
        self.fields['ingredients'].disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
