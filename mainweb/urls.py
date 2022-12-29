from django.urls import path
from .import views as admin_views
 
urlpatterns = [
  
        path('',admin_views.dashboard, name="dash"),
        path('customers',admin_views.custom_list, name="customer_list"),
        
 ]