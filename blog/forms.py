from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',
            'comment': 'Comment'
        }
