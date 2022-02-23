from email import message
from django.shortcuts import render, redirect
from . forms import UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import views as auth_views 
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

def register(request):

    if request.method == 'POST':
        print('posting')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('its saving')
            form.save()
            messages.success(request, f'Your Account has been created! Login here')
            return redirect('dashboard')  
    else:
        form = UserRegistrationForm() 
    
    return render(request, 'authentication/register.html', { 'form' : form }) 