
from .models import Comment, ImagePost
from django import forms


class CommentForm(forms.ModelForm):
    """
    Creates a form for :model:`blog.Comment` to create comments
    """
    class Meta:
        model = Comment
        fields = ('body',)


class UserPostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = [
            'title', 'slug', 'image', 'description', 'status']
