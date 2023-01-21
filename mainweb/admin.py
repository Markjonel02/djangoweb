from django.contrib import admin
from. models import * #Customers_crud,Product_crud
from django.contrib.auth.admin import UserAdmin
admin.site.register(Customers_crud)
admin.site.register(Product_crud)
admin.site.register(PhotoUPporcelain)



# Register your models here.
