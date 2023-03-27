from django import forms
from .models import Comment

from django.forms import TextInput


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=TextInput(attrs={'placeholder': 'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': TextInput(attrs={'placeholder': 'Add a comment...'})
        }
