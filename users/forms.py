
from django import forms
from django.contrib.auth.models import User # importing User Model 
from django.contrib.auth.forms import UserCreationForm  # importing UserCreationForm to create form

# Defining a class for login
class LoginForm(forms.Form):    # inherits from forms.Form
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget = forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta: # Defining Meta class
        model = User    # using User's model when we add later. 
        fields = ['username', 'email', 'password1', 'password2']    # using two password to make sure they match

