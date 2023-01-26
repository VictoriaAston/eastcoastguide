from django.forms import ModelForm
from .models import Comment, Restaurant

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['user', 'date', 'comment', 'rating']
