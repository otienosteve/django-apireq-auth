from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class SilverUserForm(UserCreationForm,forms.ModelForm):
    class Meta:
        model=User  
        fields=('username','email','password1','password2')
