from django.contrib import admin
from. models import * #Customers_crud,Product_crud
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    list_display= ('email','user_name','first_name','is_staff','is_active')

admin.site.register(UserManagement)