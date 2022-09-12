from django import forms
from .models import Category, Comment, Post


class BlogForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.STATUS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category',
            'status'
        ]
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['content']
        