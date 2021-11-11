from django import forms
from . models import User,Post

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'