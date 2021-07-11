from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),label='Enter Confirm Password')
    class Meta:
        model = User
        fields = ['username','password1','password2']
        labels = {
            'username':'Enter user name',
        }
        widgets = {'username': forms.TextInput(attrs={'class': 'input'})}


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),label='Enter Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}),label='Enter Password')
