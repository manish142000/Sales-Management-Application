# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

user_type_choices = (
    ('rep', 'Sales_rep'), 
    ('admin_staff', 'Sales_admin_staff'),
    ('admin_super', 'Sales_admin_superuser') 
)

class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create(self, email, password, **extra_args):

        '''
            Function to create a user 
        '''
        if not email:
            raise ValueError(_('The Email must be set'))
        
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_args) 
        user.set_password(password) 
        user.save()
        return user 

    def createsuperuser(self, email, password, **extra_args):

        '''
            Function to create a superuser
        '''
        extra_args.setdefault('is_staff', True)
        extra_args.setdefault('is_superuser', True)
        extra_args.setdefault('is_active', True)

        if extra_args.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_args.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create(email, password, **extra_args)


class User(AbstractBaseUser, PermissionsMixin):

    username = None 
    created_at = models.DateTimeField(auto_now=True) 
    first_name = models.CharField(max_length=255, null = True, blank=True) 
    last_name = models.CharField(max_length=255, null = True, blank=True) 
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=255, null = True, blank=True) 
    user_type = models.CharField(max_length=255, choices=user_type_choices)
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)
    manager_id = models.ForeignKey('self', null=True, on_delete=models.SET_NULL) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'{ self.email }'



