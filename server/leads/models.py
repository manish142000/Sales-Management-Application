from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Lead(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=255) 
    email_address = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=20) 
    state = models.CharField(max_length=255) 
    user_id = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f'{ self.name }'  

class Remark(models.Model):
    created_at = models.DateTimeField(auto_created=True) 
    remark = models.TextField() 
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return f'{ self.lead_id }'