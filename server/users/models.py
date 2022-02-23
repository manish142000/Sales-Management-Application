# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.
class user(AbstractUser):
    created_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    email = models.EmailField(_('email address'), unique=True)  
    phone_number = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255) 
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{ self.username }'