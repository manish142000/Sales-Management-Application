from django.contrib import admin

# Register your models here.
from users.models import User


admin.site.site_header = 'Leads Management Platform'

class UserAdmin(admin.ModelAdmin):
    exclude = ('title', 'password')
    list_display = ('email', 'created_at')
    list_filter = ['created_at']

    actions = ['approve'] 

    @admin.action(description="Approve user as Sales Representative")
    def approve(self, request, queryset):
        queryset.update(user_type = "rep") 
   

admin.site.register(User, UserAdmin) 
