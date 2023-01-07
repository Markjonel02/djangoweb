from django.urls import path
from .import views as admin_views
 
urlpatterns = [
         # customers profile urls 
        path('',admin_views.dashboard, name="dash"),
        # CRUD 
        path('customers/',admin_views.custom_list, name="customer_list"),
        path('edit/<int:pk>/',admin_views.edit_customers,name="customer_edit"),
        path('del/<int:pk>/',admin_views.del_customers,name='customer_del'),
        
        # product management urls 
        path('prod/',admin_views.product_list,name='product_list'),
        path('prod_edit/<int:pk>/',admin_views.product_edit,name='product_edit'),
        path('delete/<int:pk>/',admin_views.product_del,name='product_del'),
        path('archive/',admin_views.archive,name='prod_arch'),

        
        
 ]