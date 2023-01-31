from django import forms 
from .models import *


class MakePost(forms.ModelForm):
    class Meta: 
        model=Post
        fields=['title', 'message']

class MakeComment(forms.ModelForm):
    class Meta: 
        model=Comments
        fields=['message']

class UpdateComment(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['post', 'message']
