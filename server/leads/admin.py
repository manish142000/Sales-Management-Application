from django.contrib import admin

# Register your models here.
from .models import Lead, Remark
admin.site.register(Lead)
admin.site.register(Remark) 
