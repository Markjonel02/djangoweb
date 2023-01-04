from django.urls import path
from .import views as admin_views
 
urlpatterns = [
         #crud customers profile urls 
        path('',admin_views.dashboard, name="dash"),
        path('customers/',admin_views.custom_list, name="customer_list"),
        path('edit/<int:pk>/',admin_views.edit_customers,name="customer_edit"),
        path('del/<int:pk>/',admin_views.del_customers,name='customer_del'),
        
        # crud product management urls 
        path('prod/',admin_views.product_management,name='product'),

        
 ]