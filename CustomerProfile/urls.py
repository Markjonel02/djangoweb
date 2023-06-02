from django.urls import path
from .import views

urlpatterns = [
    path('customer', views.customer_list, name="customer_list"),
    path('delete_customer/<int:id>/',views.del_customers, name="del_customer"),
    path('update/<int:id>/',views.customer_edit, name="edit_customer"),
    
]