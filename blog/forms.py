from django import forms
from .models import Comment, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['content']
        