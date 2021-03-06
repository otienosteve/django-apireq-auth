from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Post

class LoginForm(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class CustomRegisterForm(UserCreationForm,forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','last_name','password1','password2')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('__all__')