from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import user 
from django import forms 

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2'] 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')