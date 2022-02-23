from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . views import LoginView


urlpatterns = [
    path('', LoginView.as_view(template_name = 'authentication/login.html'), name = 'dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'authentication/logout.html'), name = "logout" ),
    path('register/', views.register, name='register'),
] 